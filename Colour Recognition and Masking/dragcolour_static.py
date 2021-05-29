import numpy as np
import cv2
def nothing(x):
    print("value changed")
frame=cv2.imread("rgb1.png")
cv2.namedWindow('test')
cv2.createTrackbar('R','test',0,180,nothing)
cv2.createTrackbar('G','test',0,255,nothing)
cv2.createTrackbar('B','test',0,255,nothing)
while(1):
    frame=cv2.imread("rgb1.png")
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    k=cv2.waitKey(1)
    if k==27:
        break
    r=cv2.getTrackbarPos('R','test')
    g=cv2.getTrackbarPos('G','test')
    b=cv2.getTrackbarPos('B','test')
    

    lower=np.array([r,g,b])
    higher=np.array([180,255,255])

    mask=cv2.inRange(hsv,lower,higher)

    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


cv2.destroyAllWindows()

