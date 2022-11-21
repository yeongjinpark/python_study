import cv2

cap=cv2.VideoCapture(0)

if(cap.isOpened()):
    print("FaceTime")
    while(cv2.waitKey(3) != ord('q')):
        ret,frame=cap.read()
        cv2.imshow("webCam",frame)


else:
    print("webCam is failed to use")

cap.release()
cv2.destroyAllwindows()
