import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import random
import os

# Initialize text-to-speech
engine = pyttsx3.init()

# Define dataset path
base_dir = 'dataset'

# Classes and their corresponding folders
classes = ['apple', 'banana', 'cherry', 'dragon fruit']
image_paths = {fruit: [os.path.join(base_dir, fruit, file) for file in os.listdir(os.path.join(base_dir, fruit))] for fruit in classes}

# Function to display a random image
def display_random_image():
    # Randomly pick a class
    fruit = random.choice(classes)
    # Randomly pick an image from the class folder
    image_path = random.choice(image_paths[fruit])
    
    # Load and display the image
    img = Image.open(image_path).resize((300, 300))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img
    
    # Display the label
    fruit_label.set(fruit.capitalize())
    
    # Convert label to speech
    engine.say(f"It is {fruit}")
    engine.runAndWait()

# GUI Setup
root = tk.Tk()
root.title("Fruit Classifier")

# Image display label
image_label = tk.Label(root)
image_label.pack()

# Text label
fruit_label = tk.StringVar()
label_text = tk.Label(root, textvariable=fruit_label, font=("Helvetica", 20))
label_text.pack()

# Button to trigger random image display
button = tk.Button(root, text="Show Random Fruit", command=display_random_image)
button.pack()

# Start the application
root.mainloop()
