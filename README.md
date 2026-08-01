# 🧿 OculusAI

## AI-Powered Vision Assistant for the Visually Impaired

OculusAI is an intelligent computer vision application designed to assist visually impaired individuals by providing real-time environmental awareness through artificial intelligence. By combining state-of-the-art object detection with voice assistance, OculusAI aims to enhance independence, situational awareness, and everyday navigation.

The application processes live video from a camera, identifies surrounding objects, and will ultimately provide contextual audio feedback to help users better understand their environment.

---

## Features

### Current Features

* Real-time live video streaming via DroidCam or webcam
* Object detection using YOLOv8
* Live object annotation with bounding boxes
* Confidence-based detection filtering
* Interactive Streamlit user interface
* Efficient real-time processing

---

## Planned Features

* Live object information panel
* Voice feedback using text-to-speech
* Duplicate detection suppression
* Object counting
* Object tracking
* Directional guidance (Left, Centre, Right)
* Distance estimation
* Scene understanding
* Navigation assistance
* Detection history
* Performance analytics
* Customisable confidence threshold
* Modern user interface enhancements

---

## Technologies Used

* Python
* Streamlit
* OpenCV
* Ultralytics YOLOv8
* NumPy
* Pandas
* Pillow
* pyttsx3

---

## Project Structure

```text
Oculus/
│
├── OculusAI.py
├── README.md
├── requirements.txt
├── assets/
├── screenshots/
└── models/
```

---

## Installation

Clone the repository, install the required dependencies, and launch the application using Streamlit.

---

## Project Vision

The long-term objective of OculusAI is to develop a comprehensive AI-powered vision assistant capable of understanding its surroundings in real time, recognising important objects, estimating their positions and distances, and providing meaningful spoken guidance to visually impaired users.

Future development will incorporate object tracking, scene interpretation, intelligent navigation assistance, and contextual decision-making, transforming OculusAI into a practical and reliable accessibility solution.

---

## Current Development Status

**Under Active Development**

### Completed

* Streamlit interface
* Live camera integration
* YOLOv8 object detection
* Real-time annotated video
* Confidence threshold filtering

### In Progress

* Detection table
* Object management
* Voice assistance

### Planned

* Object tracking
* Scene understanding
* Navigation mode
* Advanced AI assistance

---

## Author

Developed by **Elvin Pillay**

Bachelor of Technology in Computer Science and Engineering (Artificial Intelligence & Machine Learning)

---

## Licence

This project is intended for educational, research, and accessibility purposes.
