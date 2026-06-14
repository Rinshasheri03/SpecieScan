# SpecieScan
Butterfly Identification using AI

🦋 SpeciesScan – Butterfly Species Identification using CNN
📌 Project Overview

SpeciesScan is a deep learning-based web application that identifies butterfly species from images. The system uses a Convolutional Neural Network (CNN) trained on butterfly datasets to classify species with high accuracy.

This project is designed to help students, researchers, and nature enthusiasts quickly identify butterfly species using image input.

🎯 Objective
To build an AI model that can classify butterfly species from images.
To apply Deep Learning (CNN) for image recognition.
To develop a simple web interface for real-time prediction.
🧠 Technology Used
Python 🐍
TensorFlow / Keras 🤖
Convolutional Neural Network (CNN)
OpenCV (Image Processing)
Flask (Web Framework) (if used)
HTML, CSS (Frontend)
NumPy, Pandas
🗂️ Project Structure
SpeciesScan/
│
├── dataset/                 # Butterfly image dataset
├── model/                   # Trained CNN model
│   └── butterfly_model.h5
├── static/                  # CSS, JS, images
├── templates/              # HTML files
├── app.py                  # Flask web application
├── train_model.py          # CNN training script
├── requirements.txt        # Required dependencies
├── README.md               # Project documentation
└── .gitignore              # Files to ignore in Git
🧪 How It Works
User uploads a butterfly image.
Image is preprocessed (resized, normalized).
CNN model extracts features from the image.
Model predicts the butterfly species.
Result is displayed on the web interface.
🧠 Model Architecture (CNN)
Input Layer (Image input)
Convolutional Layers
Max Pooling Layers
Flatten Layer
Dense Fully Connected Layers
Output Layer (Softmax classification)
🚀 Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/SpeciesScan.git
cd SpeciesScan
2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py

Then open:

http://127.0.0.1:5000/
📊 Results
Achieved high accuracy using CNN model
Improved performance compared to RNN/LSTM approaches
Fast and reliable prediction on butterfly images
📷 Sample Output

(Add screenshots of your project here)

🔮 Future Improvements
Increase dataset size for better accuracy
Deploy model on cloud (AWS / Render / HuggingFace)
Add mobile app version
Improve UI for better user experience
Add more insect species classification
👨‍💻 Author

Rinsha Sherin
Computer Science Student
Passionate about AI, ML, and Web Development