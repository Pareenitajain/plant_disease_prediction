import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# =========================
# PATHS (IMPORTANT)
# =========================
MODEL_PATH = "model/plant_disease_model.h5"
TEST_DIR = "dataset/test"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Test data generator
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

# Predict
y_pred_probs = model.predict(test_generator)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = test_generator.classes

class_names = list(test_generator.class_indices.keys())

# =========================
# Classification Report
# =========================
print("\n===== Classification Report =====\n")
print(classification_report(y_true, y_pred, target_names=class_names))

# =========================
# Confusion Matrix
# =========================
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(14, 12))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)

plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix - Plant Disease Prediction")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.show()
