from ultralytics import YOLO
import cv2
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Dynamically select a valid voice
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # Use the second voice if available
else:
    engine.setProperty('voice', voices[0].id)  # Default to the first voice

engine.setProperty('rate', 130)  # Adjust speech rate

# Load the YOLO model
model = YOLO("yolov8s.pt")  # Ensure the model file is in the same directory or provide the correct path


def SpeakText(command):
    """Speak the given text using TTS."""
    engine.say(command)
    engine.runAndWait()


def object_detection():
    """Continuously detect a user-specified object using a webcam."""
    cap = cv2.VideoCapture(0)  # Open webcam (0 is usually the default camera)
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    SpeakText("Camera turned on. Type an object to detect.")
    print("Type an object label to detect (e.g., 'person', 'chair'). Press 's' to stop and enter a new label.")

    object_to_detect = input("Enter object to detect: ").lower().strip()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Perform YOLO predictions
        result = model.predict(frame, show=False)

        detected_objects = []
        for res in result:
            for indx in range(len(res.boxes.conf.tolist())):
                if res.boxes.conf[indx] > 0.50:  # Confidence threshold
                    obj_nm = res.boxes.cls.tolist()[indx]
                    obj_label = model.names[obj_nm]
                    if obj_label.lower() == object_to_detect:
                        detected_objects.append(obj_label)

        # Speak and display the results if the object is found
        if detected_objects:
            msg = f"Detected {len(detected_objects)} {object_to_detect}(s)."
            print(msg)
            SpeakText(msg)

        # Show the webcam feed
        cv2.putText(frame, f"Looking for: {object_to_detect}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Webcam Feed", frame)

        # Press 's' to stop and enter a new object
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            print("Stopping detection. Enter a new label or type 'stop' to quit.")
            object_to_detect = input("Enter object to detect: ").lower().strip()
            if object_to_detect == "stop":
                break

        # Press 'q' to quit immediately
        if key == ord('q'):
            break

    # Release the video capture object and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


# Run the object_detection function
object_detection()
