import cv2
import numpy as np

cap=cv2.VideoCapture(0)

if(cap.isOpened()):
    print("webCam opened")
    while(cv2.waitKey(3) != ord('q')):
        ret, frame=cap.read()

        edges=cv2.Canny(frame,100,200)
        cv2.imshow('edges',edges)


else:
    print("opening webcam failed")

cap.release()
cv2.destoryAllWindows()
