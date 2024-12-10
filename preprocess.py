import cv2
import os

# Set the desired size
new_size = (224, 224)  # adjust this to your desired size

# Define the path to your dataset
dataset_path = 'dataset'

# Iterate through the subfolders
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if os.path.isdir(folder_path):
        # Iterate through the images in the subfolder
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                img_path = os.path.join(folder_path, filename)
                # Load the image
                img = cv2.imread(img_path)
                # Resize the image
                resized_img = cv2.resize(img, new_size)
                # Save the resized image
                cv2.imwrite(img_path, resized_img)