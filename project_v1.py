import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Hand detector initialization

    # Check for spread index and middle fingers to detect V gesture

    # Add photo capture code

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()