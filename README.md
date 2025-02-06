# vizhi-prototype-yolo
## YOLO Object Detection with Text-to-Speech (TTS) and Dynamic Object Selection based on user input

This project demonstrates real-time object detection using **YOLOv8** and provides audio feedback using a text-to-speech (TTS) engine. The application allows users to specify an object to detect and continuously monitors the webcam feed for that object.

## Features
- **YOLOv8 Integration**: Uses the YOLOv8 model for efficient object detection.
- **Real-Time Detection**: Continuously detects objects from the webcam feed.
- **Text-to-Speech Feedback**: Speaks out the number of detected objects for better accessibility.
- **Dynamic Object Selection**: Allows users to change the object to detect during runtime.
- **Easy Controls**: 
  - Press **'s'** to stop and enter a new object to detect.
  - Press **'q'** to quit the application.

## Prerequisites
Before running the project, ensure the following are installed:
1. **Python 3.x**
2. Required Python libraries:
   - `ultralytics` (for YOLOv8)
   - `opencv-python` (for webcam feed and video processing)
   - `pyttsx3` (for text-to-speech functionality)

   Install these using:
   ```bash
   pip install ultralytics opencv-python pyttsx3
   ```
3. Yolov8 model

## **How to Use**
**1. Clone the repository or copy the code into a Python file, e.g., object_detection.py.**

```bash
https://github.com/kevin-giftson/vizhi-prototype-yolo.git
cd vizhi-prototype-yolo
```
**2. Run the script:**

```bash
python cam_type.py
```
**3. Follow the instructions:**

- The program will prompt you to enter the name of the object to detect (e.g., person, chair, etc.).
- The webcam feed will display, and the application will start detecting the specified object.

**4. Controls:**

- 's': Stop detection and input a new object to detect.
- 'q': Quit the application.
