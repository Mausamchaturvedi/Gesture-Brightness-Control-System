# ✋ Gesture Brightness Control System

## 📌 Project Overview

**Gesture Brightness Control System** is a Python-based computer vision project that allows users to control their computer's screen brightness using simple hand gestures.

The system uses a webcam to detect hand movements with **MediaPipe Hand Landmarker** and **OpenCV**. It calculates the distance between the thumb tip and index finger tip and converts that distance into a brightness percentage.

Users can increase or decrease screen brightness simply by moving their fingers closer together or farther apart, without using a keyboard or mouse.

## ✨ Features

- ✋ Real-time hand gesture detection using a webcam.
- 📷 Live hand tracking using OpenCV and MediaPipe.
- ☀️ Control system brightness using thumb and index finger distance.
- 📊 Real-time brightness percentage display.
- 🟢 Visual indicator when fingers are close together.
- 📥 Automatic download of the MediaPipe hand landmark model.
- ⚡ Simple and touch-free brightness adjustment.
- 🖥️ Live brightness bar visualization.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam access and image processing |
| MediaPipe | Hand detection and landmark tracking |
| NumPy | Brightness level calculations |
| Math | Distance calculation between fingers |
| Screen Brightness Control | Adjusting system brightness |

## 📂 Project Structure

```text
Gesture-Brightness-Control/
│
├── brightness_control.py
├── hand_landmarker.task
├── README.md
└── requirements.txt
```

**Note:** The `hand_landmarker.task` file is downloaded automatically when you run the program if it is not already available.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Gesture-Brightness-Control.git
```

### 2. Navigate to the Project Directory

```bash
cd Gesture-Brightness-Control
```

### 3. Install Required Libraries

```bash
pip install opencv-python mediapipe numpy screen-brightness-control
```

### 4. Run the Project

```bash
python brightness_control.py
```

## 🎮 How It Works

1. Start the Python program.
2. Allow webcam access.
3. Show your hand in front of the webcam.
4. The system detects your thumb tip and index finger tip.
5. It calculates the distance between these two fingertips.
6. The distance is converted into a brightness value between 0% and 100%.
7. Your computer's screen brightness changes automatically.

### Gesture Controls

| Hand Gesture | Brightness |
|---|---|
| Fingers close together | Decrease brightness |
| Fingers move apart | Increase brightness |
| Fingers at maximum distance | Higher brightness |

## 🧠 Working Principle

The project uses MediaPipe to identify two important hand landmarks:

- **Landmark 4:** Thumb Tip
- **Landmark 8:** Index Finger Tip

The distance between these landmarks is calculated using the Euclidean distance formula:

```python
length = math.hypot(x2 - x1, y2 - y1)
```

The distance is then mapped to a brightness range of 0 to 100 using NumPy's interpolation function.

```python
bright_level = np.interp(
    length,
    [20, 200],
    [0, 100]
)
```

Finally, the brightness is applied to the system:

```python
sbc.set_brightness(int(bright_level))
```

## 📋 Requirements

- Python 3.9 or compatible version supported by the installed MediaPipe release.
- Working webcam.
- Windows, macOS, or Linux (brightness-control support depends on the operating system and hardware).
- Required Python libraries.

## 🚀 Future Enhancements

- Support for multiple hand gestures.
- Add volume control using hand gestures.
- Add gesture-based mouse control.
- Improve brightness adjustment accuracy.
- Add a graphical user interface (GUI).
- Add support for additional gesture-based system controls.

## 🎯 Applications

- Touch-free computer control.
- Smart desktop environments.
- Human-computer interaction.
- Accessibility solutions.
- Computer vision applications.
- Gesture recognition systems.

## 👨‍💻 Author

**Mausam Chaturvedi**

Python | Computer Vision | OpenCV | MediaPipe

## 📜 License

This project is developed for educational and learning purposes. You are welcome to explore, modify, and improve the project.

---

⭐ If you find this project useful, don't forget to give this repository a star!
