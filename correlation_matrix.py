import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

DATASET_PATH = "dataset/train"

data = []

for class_name in os.listdir(DATASET_PATH):
    class_path = os.path.join(DATASET_PATH, class_name)
    if not os.path.isdir(class_path):
        continue

    for img_name in tqdm(os.listdir(class_path), desc=class_name):
        img_path = os.path.join(class_path, img_name)

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        img = cv2.resize(img, (224, 224))

        data.append({
            "Class": class_name,
            "Mean": np.mean(img),
            "Std": np.std(img),
            "Min": np.min(img),
            "Max": np.max(img)
        })

# Create DataFrame
df = pd.DataFrame(data)

# 🔥 Aggregate features per class (VERY IMPORTANT)
class_features = df.groupby("Class").mean()

# Compute correlation between classes
corr_matrix = class_features.T.corr()

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(
    corr_matrix,
    cmap="coolwarm",
    annot=False
)

plt.title("Class-wise Correlation Matrix (Plant Disease Categories)")
plt.tight_layout()
plt.show()
