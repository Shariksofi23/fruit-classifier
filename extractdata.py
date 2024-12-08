import cv2
import numpy as np
import os
import pandas as pd

def extract_features(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (100, 100))  # Resize for consistency
    # Compute color histogram
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

data = []
labels = []

base_dir = 'dataset'
classes = ['apple', 'banana', 'cherry', 'dragon fruit']

for label, fruit in enumerate(classes):
    folder = os.path.join(base_dir, fruit)
    for file in os.listdir(folder):
        try:
            filepath = os.path.join(folder, file)
            features = extract_features(filepath)
            data.append(features)
            labels.append(label)
        except:
            continue

# Save as CSV
df = pd.DataFrame(data)
df['label'] = labels
df.to_csv('fruit_features.csv', index=False)
