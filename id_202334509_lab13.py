import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('C:\\Users\\user\\Desktop\\Liz.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.01, 4, minSize = (30,30))

for (x, y, w, h) in faces:
    print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

print('number of cats in image=', len(faces))

cv2.imshow('img', img)
cv2.waitKey()
