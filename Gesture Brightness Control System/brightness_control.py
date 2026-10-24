import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import math
import numpy as np
import screen_brightness_control as sbc
import os
import urllib.request

# MediaPipe Handq Landmarker Model Setup
model_path = "hand_landmarker.task"

if not os.path.exists(model_path):
    print("Downloading hand_landmarker model file...")

    url = (
        "https://storage.googleapis.com/"
        "mediapipe-models/hand_landmarker/"
        "hand_landmarker/float16/1/hand_landmarker.task"
    )

    urllib.request.urlretrieve(url, model_path)

    print("Model downloaded successfully!")


# MediaPipe options
BaseOptions = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)

# Create hand detector
detector = HandLandmarker.create_from_options(options)

# Webcam Initialize
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


bright_bar = 400
bright_per = 0

print("Camera starting...")
print("Press 'q' to exit.")

# Main Loop
while cap.isOpened():

    success, img = cap.read()

    if not success:
        print("Camera frame not available.")
        break

    # Flip image for mirror effect
    img = cv2.flip(img, 1)

    # Get image dimensions
    h, w, c = img.shape

    # OpenCV BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert image to MediaPipe format
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=img_rgb
    )

    # Hand Detection
    detection_result = detector.detect(mp_image)

    if detection_result.hand_landmarks:

        for hand_landmarks in detection_result.hand_landmarks:

            # Landmark 4 = Thumb Tip
            # Landmark 8 = Index Finger Tip

            x1 = int(hand_landmarks[4].x * w)
            y1 = int(hand_landmarks[4].y * h)

            x2 = int(hand_landmarks[8].x * w)
            y2 = int(hand_landmarks[8].y * h)

            # Draw thumb point
            cv2.circle(
                img,
                (x1, y1),
                10,
                (255, 0, 0),
                cv2.FILLED
            )

            # Draw index finger point
            cv2.circle(
                img,
                (x2, y2),
                10,
                (255, 0, 0),
                cv2.FILLED
            )

            # Draw line between thumb and index finger
            cv2.line(
                img,
                (x1, y1),
                (x2, y2),
                (255, 0, 255),
                3
            )

            # Center point
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            # Calculate Distance
            length = math.hypot(
                x2 - x1,
                y2 - y1
            )

            # Convert Distance to Brightness
            bright_level = np.interp(
                length,
                [20, 200],
                [0, 100]
            )

            bright_bar = np.interp(
                length,
                [20, 200],
                [400, 150]
            )

            bright_per = np.interp(
                length,
                [20, 200],
                [0, 100]
            )

            # Keep brightness between 0 and 100
            bright_level = max(
                0,
                min(100, bright_level)
            )

            # Change System Brightness
            try:
                sbc.set_brightness(int(bright_level))
            except Exception:
                pass


            # Show Green Circle When Fingers Are Close

            if length < 20:
                cv2.circle(
                    img,
                    (cx, cy),
                    10,
                    (0, 255, 0),
                    cv2.FILLED
                )

    # Brightness Bar UI

    # Outer brightness bar
    cv2.rectangle(
        img,
        (50, 150),
        (85, 400),
        (0, 255, 0),
        3
    )

    # Filled brightness bar
    cv2.rectangle(
        img,
        (50, int(bright_bar)),
        (85, 400),
        (0, 255, 0),
        cv2.FILLED
    )

    # Brightness percentage
    cv2.putText(
        img,
        f"{int(bright_per)} %",
        (40, 450),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (255, 255, 255),
        3
    )

    # Display window
    cv2.imshow(
        "Gesture Brightness Control System",
        img
    )

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release Resources
cap.release()
cv2.destroyAllWindows()
detector.close()