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

