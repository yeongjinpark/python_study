import cv2
import numpy as np

cap=cv2.VideoCapture(0)

if(cap.isOpened()):
    print("webCam opened")
    while(cv2.waitKey(3) != ord('q')):
        ret, frame=cap.read()

        hsv_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lowBound=np.array([110,50,50])
        upBound=np.array([130,255,255])
        mask=cv2.inRange(hsv_image,lowBound,upBound)
        kernel=np.ones((5,5),np.uint8)
        mask=cv2.dilate(mask,kernel,iterations=1)
        h1,w1=mask.shape
        h2,w2,d2=frame.shape
        imgCam=np.zeros((max([h1,h2]),w1+w2,3),dtype='uint8')
        imgCam[:h1,:w1,0]=mask
        imgCam[:h1,:w1,1]=mask
        imgCam[:h1,:w1,2]=mask
        imgCam[:h2,w1:w1+w2,:]=np.dstack([frame])

        imgCam=cv2.resize(imgCam,(w1,h1),interpolation=cv2.INTER_LINEAR)
        cv2.imshow("webcam",imgCam)




cap.release()
cv2.destoryAllWindows()
