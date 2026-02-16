# 🌿 Plant Disease Prediction System

A comprehensive web application for detecting plant diseases using deep learning, providing treatment recommendations, and locating nearby pesticide stores.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Disease Information](#disease-information)
- [API Documentation](#api-documentation)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The Plant Disease Prediction System is an AI-powered web application that helps farmers and agricultural professionals identify plant diseases through image analysis. The system provides:

- **Accurate Disease Detection**: Using a trained CNN model to identify plant diseases
- **Comprehensive Information**: Detailed disease descriptions, symptoms, and prevention tips
- **Treatment Recommendations**: Both chemical and organic treatment options
- **Medicine Suggestions**: Specific product recommendations
- **Store Locator**: Find nearby pesticide and agricultural supply stores
- **User Authentication**: Secure login system with SQLite database

## ✨ Features

### 🔐 User Authentication
- User registration with email validation
- Secure login (username or email)
- Password hashing using SHA-256
- Session-based authentication
- Protected routes

### 🤖 Disease Prediction
- Image upload (PNG, JPG, JPEG)
- Real-time disease detection using TensorFlow/Keras
- Confidence score display
- Support for multiple plant diseases

### 📚 Disease Information
- Detailed disease descriptions
- Symptom identification
- Chemical treatment options
- Organic treatment alternatives
- Prevention tips and best practices
- Specific medicine recommendations

### 🏪 Store Locator
- Browser geolocation integration
- Google Maps integration
- Find nearby pesticide stores
- Agricultural supply store search

### 🎨 Modern UI/UX
- Responsive design
- Gradient backgrounds
- Smooth animations
- Mobile-friendly interface
- Flash message notifications

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **TensorFlow/Keras**: Deep learning model
- **SQLite3**: User database
- **Werkzeug**: File handling and security

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with gradients and animations
- **JavaScript**: Geolocation and interactivity

### Machine Learning
- **CNN Architecture**: Convolutional Neural Network
- **Input Size**: 224x224 pixels
- **Image Preprocessing**: Normalization and resizing

## 📁 Project Structure

```
plant_disease_prediction/
│
├── app.py                      # Main Flask application
├── database.py                 # Database operations
├── disease_info.py             # Disease information database
├── predict.py                  # Standalone prediction script
├── train_model.py              # Model training script
├── requirements.txt            # Python dependencies
│
├── model/
│   └── plant_disease_model.h5  # Trained CNN model
│
├── dataset/
│   ├── train/                  # Training images
│   └── test/                   # Testing images
│
├── static/
│   ├── css/
│   │   └── style.css          # Application styles
│   └── uploads/               # Uploaded images
│
├── templates/
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── upload.html            # Image upload page
│   └── result.html            # Prediction results page
│
└── plant_disease.db           # SQLite database (auto-generated)
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd plant_disease_prediction
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Model
Ensure the trained model exists at `model/plant_disease_model.h5`

### Step 4: Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## 📖 Usage

### 1. Register an Account
- Navigate to `http://127.0.0.1:5000/register`
- Fill in username, email, and password
- Click "Register"

### 2. Login
- Go to `http://127.0.0.1:5000/login`
- Enter username/email and password
- Click "Login"

### 3. Upload Plant Image
- Click the upload area
- Select a plant image (PNG, JPG, or JPEG)
- Image will be automatically processed

### 4. View Results
- See predicted disease name
- View confidence score
- Read disease information
- Check treatment recommendations
- View medicine suggestions
- Read prevention tips

### 5. Find Nearby Stores
- Click "Find Stores Near Me"
- Allow location access
- View nearby pesticide stores on Google Maps

## 🦠 Disease Information

The system currently supports detection and information for:

### Supported Diseases

1. **Pepper Bell Bacterial Spot**
   - Caused by Xanthomonas bacteria
   - Treatments: Copper-based bactericides, Mancozeb, Neem oil
   - Medicines: Kocide 3000, Champion WP, Mancozeb 75% WP

2. **Tomato Bacterial Spot**
   - Bacterial disease affecting tomato plants
   - Treatments: Copper sprays, Streptomycin, Neem oil
   - Medicines: Copper Oxychloride 50% WP, Streptocycline

3. **Potato Early Blight**
   - Fungal disease (Alternaria solani)
   - Treatments: Chlorothalonil, Mancozeb, Azoxystrobin
   - Medicines: Mancozeb 75% WP, Chlorothalonil 75% WP

4. **Tomato Late Blight**
   - Devastating fungal disease (Phytophthora infestans)
   - Treatments: Metalaxyl + Mancozeb, Copper fungicides
   - Medicines: Ridomil Gold, Curzate, Bordeaux mixture

5. **Tomato Leaf Mold**
   - Common in greenhouse tomatoes (Passalora fulva)
   - Treatments: Chlorothalonil, Mancozeb, Improved ventilation
   - Medicines: Mancozeb 75% WP, Copper Oxychloride

## 🔌 API Documentation

### Routes

#### Authentication Routes

**POST /register**
- Register a new user
- Body: `username`, `email`, `password`, `confirm_password`
- Returns: Redirect to login on success

**POST /login**
- Authenticate user
- Body: `username` (or email), `password`
- Returns: Redirect to upload page on success

**GET /logout**
- Clear user session
- Returns: Redirect to login page

#### Application Routes

**GET /upload**
- Display upload page (requires authentication)
- Returns: Upload page template

**POST /upload**
- Upload and process plant image
- Body: `file` (multipart/form-data)
- Returns: Redirect to result page

**GET /result**
- Display prediction results (requires authentication)
- Returns: Result page with disease information

## 🎨 Screenshots

### Login Page
Modern gradient design with professional form styling

### Upload Page
Clean interface with drag-and-drop upload area

### Result Page
Comprehensive disease information with:
- Uploaded image display
- Disease name and confidence score
- Disease description
- Symptoms list
- Treatment recommendations (chemical & organic)
- Medicine suggestions
- Prevention tips
- Store locator

## 🔒 Security Features

- **Password Hashing**: SHA-256 encryption
- **Session Management**: Secure session handling
- **Protected Routes**: Login required for sensitive pages
- **File Validation**: Allowed file types only
- **Secure Filenames**: Werkzeug secure filename handling
- **File Size Limit**: 16MB maximum upload size

## 🌐 Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Opera

**Note**: Geolocation feature requires HTTPS in production

## 📊 Model Information

### Architecture
- **Type**: Convolutional Neural Network (CNN)
- **Input Shape**: 224x224x3
- **Layers**: 
  - 3 Convolutional layers (32, 64, 128 filters)
  - MaxPooling layers
  - Flatten layer
  - Dense layer (128 units)
  - Dropout (0.5)
  - Output layer (softmax)

### Training
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Metrics**: Accuracy
- **Data Augmentation**: Rotation, zoom, horizontal flip

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- TensorFlow team for the deep learning framework
- Flask team for the web framework
- Agricultural experts for disease information
- Open-source community

## 📞 Support

For support, email your-email@example.com or open an issue in the repository.

## 🔮 Future Enhancements

- [ ] Support for more plant diseases
- [ ] Mobile application (Android/iOS)
- [ ] Multi-language support
- [ ] Disease history tracking
- [ ] Export reports as PDF
- [ ] Integration with weather data
- [ ] Community forum for farmers
- [ ] Expert consultation booking
- [ ] Crop management recommendations
- [ ] Pest detection feature

## 📈 Version History

### Version 1.0.0 (Current)
- User authentication system
- Disease prediction with CNN model
- Comprehensive disease information
- Treatment recommendations
- Medicine suggestions
- Store locator feature
- Responsive web design

---

**Made with ❤️ for farmers and agricultural professionals**
