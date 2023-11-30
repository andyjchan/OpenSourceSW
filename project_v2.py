import cv2
import numpy as np
import socket
import pickle
from cvzone.HandTrackingModule import HandDetector

# 길이
width, height = 1280, 720

# 캠
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# 손 탐지기
detector = HandDetector(maxHands=1, detectionCon=0.8)

# 통신 탐지기
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

# 이미지 카운터 초기화
img_counter = 0
hand_gesture_captured = False  # 손가락을 5개 펼친 상태를 기록하는 변수

while True:
    # 웹캠에서 프레임 가져오기
    success, img = cap.read()
    # 손
    hands, img = detector.findHands(img)

    data = []
    # 랜드마크 값 (x, y, z)*21
    if hands:
        # 첫 번째 손가락 탐색기 얻기
        hand = hands[0]
        # 랜드마크 목록 얻기
        lmList = hand['lmList']
        # print(lmList)
        for lm in lmList:
            data.extend([lm[0], height - lm[1], lm[2]])
        # print(data)
        # 데이터를 바이트로 인코딩하여 전송
        sock.sendto(pickle.dumps(data), serverAddressPort)

        # 손가락이 5개 펼쳐져 있다면 화면 캡쳐
        if len(lmList) == 21 and lmList[8][1] > lmList[6][1] and lmList[12][1] > lmList[10][1]:
            hand_gesture_captured = True
        else:
            # 손가락을 5개 펼친 상태에서 주먹을 쥐었을 때 화면 캡쳐하지 않음
            if hand_gesture_captured and lmList[8][1] < lmList[6][1] and lmList[12][1] < lmList[10][1]:
                img_name = f"captured_image_{img_counter}.png"
                cv2.imwrite(img_name, img)
                print(f"{img_name} saved")
                img_counter += 1
                hand_gesture_captured = False  # 상태 초기화

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)

    # 'q' 키를 누르면 종료
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
