import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

IMG_SIZE = 224

# Load model
model = tf.keras.models.load_model("model/plant_disease_model.h5")

# Load class names
train_dir = "dataset/train"
class_names = sorted(os.listdir(train_dir))

# Image path (change this)
img_path = "E:\\plant_disease_prediction\\dataset\\test\\Pepper__bell___Bacterial_spot\\test_leaf.JPG"

# Load and preprocess image
img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Prediction
predictions = model.predict(img_array)
predicted_class = class_names[np.argmax(predictions)]
confidence = np.max(predictions) * 100

print(f"Predicted Disease: {predicted_class}")
print(f"Confidence: {confidence:.2f}%")
