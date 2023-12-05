# Hand Gesture Recognition Photo Capture Program with OpenCV

## Overview
This program, developed by Gachon University's Open Source SW team (정성경, 신정현, 안제찬, 이시영), captures a photo when it recognizes a hand marked with a "V" gesture using OpenCV.

### Key Points
1. Allows for capturing photos with a tripod without the need for setting a timer.
2. Enables taking selfies with a designated hand motion (V shape).
3. Includes a 5-second countdown after recognizing the hand motion before capturing a picture.
4. Utilizes a reference distance between the index finger and the middle finger for accurate V-mark recognition.

### References
- [Unity][OpenCV] Implementing hand tracking in Unity (using CVzone): [Link](https://blog.naver.com/jeongmin062/223274596058)
- Test Hand Tracking & Hand Motion Recognition with MediaPipe: [Link](https://vrworld.tistory.com/12)

### Update Log
- `project_v1.py`: Project Sketch Code
- `project_v2.py`: Added Core Features
- `project_v3.py`: Added 5-second countdown function
- `project_final_complete.py`: Final Complete Version [Improved recognition accuracy]

## Library Requirements
- `openCV`: Install with `pip install opencv-python`
- `numpy`: Install with `pip install opencv-python numpy`
- `cvzone`: Install with `pip install cvzone`
- `mediapipe`: Install with `pip install mediapipe`

## How to Run
1. Open Anaconda Prompt (miniconda3).
2. Create a virtual environment: `conda create –n "Virtual environment name"`
3. Activate the virtual environment: `conda activate "Virtual environment name"`
4. Install Python 3.8: `conda install python=3.8`
5. Install the required libraries (see commands above).
6. Navigate to the folder where you downloaded the Python code.
7. Run the program by typing: `python project_final_complete.py`
   - If recognition is not accurate, adjust the distance between the index and middle fingers.
   - The captured file is stored in the folder where the Python code is located.
   - Press the 'q' key on the keyboard to end the program.

## Results
- Demo Video
https://github.com/bibleme/OpenSourceSW/assets/133957576/0f099c33-d2a7-4a13-b119-ee19fbb4c319
- captured_image_0.png
![captured_image_0.png](https://github.com/bibleme/OpenSourceSW/assets/133957576/27524d32-a5a0-47f3-84b1-a13de9c032a5)
