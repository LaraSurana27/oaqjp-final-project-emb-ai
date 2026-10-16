# Final Project

An AI-powered web application that detects emotions in text using the **IBM Watson NLP EmotionPredict API** and serves results through a **Flask** web interface.

## Project Description

This application analyzes user-submitted text and returns emotion scores for five emotions:
- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

The dominant emotion is identified and highlighted in the response.

## Project Structure

```
├── EmotionDetection/
│   ├── __init__.py                  # Package initializer
│   └── emotion_detection.py        # Core emotion detection module
├── static/
│   └── mywebscript.js              # Frontend JavaScript
├── templates/
│   └── index.html                  # Web interface HTML template
├── evidence/
│   ├── unit_test_output.txt        # Unit test results
│   ├── pylint_output.txt           # Static analysis results
│   └── package_import_output.txt   # Package import validation
├── server.py                       # Flask application server
├── test_emotion_detection.py       # Unit tests
├── 6b_deployment_test.png          # Deployment screenshot
├── 7c_error_handling_interface.png # Error handling screenshot
├── SUBMISSION_CHECKLIST.md         # Grading checklist
├── README.md                       # This file
├── LICENSE                         # License file
└── .gitignore                      # Git ignore rules
```

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip

### Install Dependencies

```bash
pip install flask requests pylint
```

## Usage

### Run the Application

```bash
python server.py
```

The application will start on `http://localhost:5000`.

### Using the Web Interface

1. Open `http://localhost:5000` in your browser.
2. Enter text in the input field.
3. Click **"Run Sentiment Analysis"**.
4. View the emotion scores and dominant emotion in the results section.

### API Endpoint

**GET** `/emotionDetector?textToAnalyze=<your text>`

Returns a formatted string with emotion scores and the dominant emotion.

## Testing

### Run Unit Tests

```bash
python -m unittest test_emotion_detection -v
```

### Run Static Code Analysis

```bash
pylint server.py
```

**Score: 10.00/10**

## Deployment

This application is designed to run within the IBM Skills Network Labs environment where the Watson NLP API endpoint is accessible. For local development, unit tests use mocked API responses.

## Technologies Used

- **Python 3.10** – Core programming language
- **Flask** – Web framework
- **IBM Watson NLP** – Emotion detection API
- **unittest** – Unit testing framework
- **PyLint** – Static code analysis

## License

This project is licensed under the Apache License 2.0 – see the [LICENSE](LICENSE) file for details.
