# MNIST Handwritten Digit Classifier

## Overview

The MNIST Handwritten Digit Classifier is a deep learning-based web application that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Users can upload an image of a handwritten digit, and the application predicts the corresponding digit in real time.


## Features

- Upload handwritten digit images
- Real-time digit prediction
- CNN-based deep learning model
- High accuracy on the MNIST dataset
- Simple and responsive web interface


## Technologies Used

### Frontend
- React.js
- HTML
- CSS
- JavaScript

### Backend
- Flask
- Python

### Machine Learning
- TensorFlow
- Keras
- OpenCV
- NumPy

### Dataset
- MNIST Handwritten Digit Dataset


## Project Structure

```text
mnist-digit-classifier/
│
├── frontend/
│   ├── src/
│   ├── public/
│
├── model/
│
├── app.py
├── package.json
├── package-lock.json
├── .gitignore
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/siri04-h/mnist-digit-classifier.git
```

### Navigate to the Project

```bash
cd mnist-digit-classifier
```

### Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### Install Frontend Dependencies

```bash
cd frontend
npm install
```

### Run the Flask Server

```bash
python app.py
```

### Start the React Application

```bash
npm start
```

---

## How It Works

1. The user uploads an image of a handwritten digit.
2. The image is converted to grayscale and resized to 28 × 28 pixels.
3. The image is normalized before being passed to the trained CNN model.
4. The model predicts the digit.
5. The predicted result is displayed on the screen.

## Model Information

- Model: Convolutional Neural Network (CNN)
- Framework: TensorFlow/Keras
- Dataset: MNIST
- Classes: Digits 0–9


## Learning Outcomes

This project helped me gain practical experience in:

- Deep Learning
- Convolutional Neural Networks
- TensorFlow and Keras
- Image Processing
- Flask API Development
- React Integration
- Frontend and Backend Communication


## Author

H Siri

Email: sirihalegouda2004@gmail.com

GitHub: https://github.com/siri04-h

LinkedIn: https://www.linkedin.com/in/siri-halegouda/

## License

This project is licensed under the MIT License.
