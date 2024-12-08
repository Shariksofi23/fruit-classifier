🍎 Fruit Classifier
A Python application that randomly selects a fruit image (apple, banana, cherry, or dragon fruit) from a dataset, displays it in a GUI, labels it with its name, and announces the name using text-to-speech (TTS).

Features
Random Image Selection: Picks a random fruit image from a dataset folder.
GUI Display: Displays the selected image in a user-friendly interface.
Text Label: Displays the name of the fruit below the image.
Text-to-Speech: Announces the name of the fruit.
Technologies Used
Python 3.6+: Programming language.
Pillow: For image processing.
pyttsx3: For text-to-speech conversion.
Tkinter: For GUI development.
Installation
Prerequisites
Ensure the following Python libraries are installed:


pip install pillow pyttsx3
Dataset Preparation
Organize your dataset folder as follows:


dataset/
├── apple/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── banana/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── cherry/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── dragon fruit/
    ├── image1.jpg
    ├── image2.jpg
    └── ...

Cloning the Repository
Clone the repository and navigate to the project directory:


git clone https://github.com/Shariksofi23/fruit-classifier.git
cd fruit-classifier

Usage

Ensure the dataset folder is in the project directory.

Run the application:

python display_conert_labelto_speech.py

Expected Behavior

A random fruit image is displayed in a GUI.

The fruit name appears below the image.

The name of the fruit is announced via text-to-speech.

Clicking the "Show Random Fruit" button displays a new random fruit image.
Project Structure

fruit-classifier/
├── app.py                # Main application script
├── dataset/              # Folder containing fruit images
└── README.md             # Project documentation

Future Improvements

Add machine learning to classify uploaded fruit images.
Enhance the GUI with additional information about the fruits.
Add more fruit categories and images to the dataset.
Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License.

Author
Developed by Sharik Mayaser.

