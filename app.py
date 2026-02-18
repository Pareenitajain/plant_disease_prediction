from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from functools import wraps
from database import init_db, register_user, validate_login
from disease_info import get_disease_info
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "plant_ai_secret"

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
IMG_SIZE = 224

# Initialize database on startup
init_db()

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model and class names
model = None
class_names = []

def load_model():
    global model, class_names
    try:
        model = tf.keras.models.load_model("model/plant_disease_model.h5")
        train_dir = "dataset/train"
        class_names = sorted(os.listdir(train_dir))
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"⚠️ Error loading model: {e}")

# Load model on startup
load_model()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('home.html', logged_in='user_id' in session)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin':
            flash('Access denied!', 'error')
            return redirect(url_for('home')) # Redirect to index/home
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form.get('username')
        password = request.form.get('password')
        
        success, user = validate_login(username_or_email, password)
        
        if success:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Login successful!', 'success')
            
            if user['role'] == 'admin':
                return redirect(url_for('admin'))
            return redirect(url_for('upload'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('login.html')

@app.route('/admin')
@login_required
@admin_required
def admin():
    from database import get_all_users
    users = get_all_users()
    return render_template('admin.html', users=users, username=session.get('username'))

@app.route('/admin/delete/<int:user_id>')
@login_required
@admin_required
def admin_delete_user(user_id):
    from database import delete_user
    delete_user(user_id)
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
        else:
            success, message = register_user(username, email, password)
            if success:
                flash(message, 'success')
                return redirect(url_for('login'))
            else:
                flash(message, 'error')
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        # Check if file was uploaded
        if 'file' not in request.files:
            flash('No file uploaded!', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            flash('No file selected!', 'error')
            return redirect(request.url)
        
        # Check if file is allowed
        if file and allowed_file(file.filename):
            # Save file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Make prediction
            if model is not None:
                try:
                    # Load and preprocess image
                    img = image.load_img(filepath, target_size=(IMG_SIZE, IMG_SIZE))
                    img_array = image.img_to_array(img)
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    # MobileNetV2 specific preprocessing
                    from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
                    img_array = preprocess_input(img_array)
                    
                    # Prediction
                    predictions = model.predict(img_array)
                    predicted_class = class_names[np.argmax(predictions)]
                    confidence = np.max(predictions) * 100
                    
                    # Store in session exactly as predicted (matches mapping)
                    session['prediction'] = predicted_class
                    session['confidence'] = f"{confidence:.2f}"
                    session['image_path'] = filename
                    
                    return redirect(url_for('result'))
                except Exception as e:
                    flash(f'Error making prediction: {str(e)}', 'error')
                    return redirect(request.url)
            else:
                flash('Model not loaded. Please contact administrator.', 'error')
                return redirect(request.url)
        else:
            flash('Invalid file type! Please upload PNG, JPG, or JPEG.', 'error')
            return redirect(request.url)
    
    return render_template('upload.html', username=session.get('username'))

@app.route('/result')
@login_required
def result():
    prediction = session.get('prediction', 'Unknown')
    confidence = session.get('confidence', '0.00')
    image_path = session.get('image_path', '')
    
    # Get disease information
    disease_info = get_disease_info(prediction)
    
    return render_template('result.html', 
                         prediction=prediction, 
                         confidence=confidence,
                         image_path=image_path,
                         disease_info=disease_info)

if __name__ == '__main__':
    app.run(debug=True)
