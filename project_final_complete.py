import cv2
import numpy as np
import socket
import pickle
import time
from cvzone.HandTrackingModule import HandDetector

# Function definition: Calculate the angle between two vectors
def calculate_angle(v1, v2):
    dot_product = np.dot(v1, v2)
    magnitudes = np.linalg.norm(v1) * np.linalg.norm(v2)
    cosine_angle = dot_product / magnitudes
    angle = np.degrees(np.arccos(cosine_angle))
    return angle

# Minimum distance between fingers for V gesture
min_finger_distance = 70

# Video dimensions
width, height = 1280, 720

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand detector initialization
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Initialize image counter
img_counter = 0
v_gesture_captured = False  # Variable to track V gesture
last_check_time = time.time()  # Last time V gesture was checked

while True:
    # Capture frame from webcam
    success, img = cap.read()
    # Detect hands
    hands, img = detector.findHands(img)

    # Get landmark values (x, y, z)*21
    if hands:
        # Get the first hand tracker
        hand = hands[0]
        # Get landmark list
        lmList = hand['lmList']

        # Check for spread index and middle fingers to detect V gesture
        if len(lmList) == 21:
            # Check distance between index and middle fingers
            dist_index_middle = np.linalg.norm(np.array(lmList[8]) - np.array(lmList[12]))

            # Consider it a V gesture only if the distance is greater than the minimum
            if dist_index_middle > min_finger_distance:
                # Vector 1: vector from lmList[6] to lmList[8]
                vector1 = np.array([lmList[8][0] - lmList[6][0], lmList[8][1] - lmList[6][1], lmList[8][2] - lmList[6][2]])
                # Vector 2: vector from lmList[10] to lmList[12]
                vector2 = np.array([lmList[12][0] - lmList[10][0], lmList[12][1] - lmList[10][1], lmList[12][2] - lmList[10][2]])

                # Calculate the angle between two vectors
                angle = calculate_angle(vector1, vector2)

                # Consider it a V gesture if it falls within a specific angle range
                if 45 < angle < 135:
                    # Check if 6 seconds have passed since the last V gesture
                    current_time = time.time()
                    if current_time - last_check_time >= 6:
                        print("V gesture detected")
                        v_gesture_captured = True

                        # Countdown for 5 seconds
                        for i in range(5, 0, -1):
                            print(f"Capturing in {i} seconds...")
                            time.sleep(1)

                        img_name = f"captured_image_{img_counter}.png"
                        cv2.imwrite(img_name, img)
                        print(f"{img_name} saved")
                        img_counter += 1
                        v_gesture_captured = False  # Reset V gesture flag
                        last_check_time = current_time  # Update last checked time

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)

    # Exit when 'q' key is pressed
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
