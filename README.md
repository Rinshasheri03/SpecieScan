# SpecieScan
Butterfly Identification using AI

SpeciesScan – Butterfly Species Identification using CNN
Project Overview

SpeciesScan is a machine learning-based application designed to identify butterfly species from images. The system uses a Convolutional Neural Network (CNN) trained on a dataset of butterfly images to classify species accurately. The project aims to demonstrate the application of deep learning in image classification and biodiversity identification.

Objective
The main objective of this project is to develop an automated system capable of identifying butterfly species from images using deep learning techniques. It also aims to provide a simple interface for users to upload images and obtain predictions in real time.

Technologies Used

. Python
. TensorFlow and Keras
. Convolutional Neural Network (CNN)
. OpenCV for image processing
. Flask for web application development (if applicable)
. HTML and CSS for frontend design
. NumPy and Pandas for data handling

Project Structure

SpeciesScan project contains the following structure

SpeciesScan
dataset directory containing training and testing images
model directory containing the trained CNN model file
static directory for CSS, JavaScript, and images
templates directory for HTML files
app.py main Flask application file
train_model.py script used to train the CNN model
requirements.txt file containing project dependencies
README.md project documentation file
gitignore file for ignoring unnecessary files in Git

Working Methodology
The user uploads a butterfly image through the application interface.
The image is preprocessed by resizing and normalization.
The trained CNN model extracts important features from the image.
The model classifies the image into a specific butterfly species.
The predicted result is displayed to the user.
Model Architecture

The CNN model used in this project consists of the following layers
Input layer for image input
Convolutional layers for feature extraction
Max pooling layers for dimensionality reduction
Flatten layer to convert feature maps into a vector
Fully connected dense layers for classification
Output layer using softmax activation for species prediction

Installation and Setup

Step 1: Clone the repository
git clone https://github.com/Rinshashei03/SpeciesScan.git
cd SpeciesScan

Step 2: Create a virtual environment
python -m venv venv
activate the environment using appropriate command for your operating system

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Run the application
python app.py

After running the application open the browser and go to
 http://0.0.0.0:8000/

Results

The model successfully classifies butterfly species with good accuracy. CNN performed better compared to other models such as RNN and LSTM for image classification tasks. The system provides fast and reliable predictions.

Future Enhancements

The project can be improved further by increasing dataset size for better accuracy, deploying the model on cloud platforms, developing a mobile application version, and expanding the system to classify other insect species.

Author

Rinsha Sherin
Computer Science Student
Interested in Machine Learning, Deep Learning, and Web Development

License

This project is intended for educational purposes and can be extended or modified as needed.