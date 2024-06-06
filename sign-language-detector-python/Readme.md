# Sign Language Detector

## Description
This project is a sign language detector using computer vision techniques. It captures hand movements through the webcam and classifies them into predefined sign language classes.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [File 1: webcam_capture.py](#file-1-webcam_capturepy)
  - [File 2: data_collection.py](#file-2-data_collectionpy)
  - [File 3: data_processing.py](#file-3-data_processingpy)
  - [File 4: sign_language_detection.py](#file-4-sign_language_detectionpy)
  - [File 5: model_training.py](#file-5-model_trainingpy)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [References](#references)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/sign-language-detector-python.git
    cd sign-language-detector-python
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### File 1: `webcam_capture.py`
This script captures video from the webcam and displays it in a window. Press 'q' to quit.

### File 2: data_collection.py
This script collects images for each class of the sign language dataset using the webcam.

### File 3: data_processing.py
This script processes collected images, extracting hand landmarks using MediaPipe and saving the processed data to a pickle file.

### File 4: sign_language_detection.py
This script captures live video from the webcam, processes the frames to detect hand landmarks, and uses a trained model to classify the sign language gestures.

### File 5: model_training.py
This script trains a RandomForestClassifier using the processed hand landmark data and saves the trained model to a pickle file.

### Project Structure
sign-language-detector-python/
├── data/
│   ├── 0/
│   ├── 1/
│   └── 2/
├── models/
│   └── model.p
├── webcam_capture.py
├── data_collection.py
├── data_processing.py
├── sign_language_detection.py
├── model_training.py
├── data.pickle
├── requirements.txt
└── README.md

### Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/new-feature).
5. Open a Pull Request.
   
### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Authors
https://github.com/computervisioneng/sign-language-detector-python

### References
OpenCV Documentation
MediaPipe Documentation

