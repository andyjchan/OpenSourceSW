import math
import cv2

src=cv2.imread("./image/road.jpg")
dst=src.copy()
gray=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray, 5000,1500,apertureSize=5, L2gradient=True)
lines=cv2.HoughLinesP(canny,0.8,math.pi/180,90,minLineLength=10,maxLineGap=100)

print('Number of detected lines =',len(lines))

for i in lines:
    cv2.line(dst, (int(i[0][0]), int(i[0][1])),(int(i[0][2]),int(i[0][3])),(0,0,255),2)

cv2.imshow("Detected Lines",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()