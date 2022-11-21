import cv2

cap=cv2.VideoCapture(0)

if(cap.isOpened()):
    print("webcam opened")
    face=cv2.CascadeClassifier('haarcascade_frontface.xml')
    eyes=cv2.CascadeClassifier('haarcascade_eye.xml')

    while(cv2.waitKey(3) != ord('q')):
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faceDetect=face.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faceDetect:
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


        cv2.imshow("webCam",frame)

else:
    print("opening video failed")

cap.release()
cv2.destroyAllWindows()
