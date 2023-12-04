import cv2
import numpy as np
import socket
import pickle
import time
from cvzone.HandTrackingModule import HandDetector

# Dimensions
width, height = 1280, 720

# Camera
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Communication socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

# Image counter initialization
img_counter = 0
hand_gesture_captured = False

while True:
    # Get frame from webcam
    success, img = cap.read()
    # Find hands
    hands, img = detector.findHands(img)

    data = []
    # Landmark values (x, y, z)*21
    if hands:
        # Get the first hand
        hand = hands[0]
        # Get landmark list
        lmList = hand['lmList']
        # print(lmList)
        for lm in lmList:
            data.extend([lm[0], height - lm[1], lm[2]])
        # print(data)
        # Encode data into bytes and send
        sock.sendto(pickle.dumps(data), serverAddressPort)

        # Capture the screen if V gesture is made
        if hand_gesture_captured and lmList[8][1] > lmList[12][1]:
	   # 5-second countdown function
            for i in range(5, 0, -1):
                print(f"Capturing in {i} seconds...")
                time.sleep(1)

            img_name = f"captured_image_{img_counter}.png"
            cv2.imwrite(img_name, img)
            print(f"{img_name} saved")
            img_counter += 1
            hand_gesture_captured = False  # Reset the state

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)

    # Press 'q' to exit
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
