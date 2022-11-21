import cv2

cap=cv2.VideoCapture("test.mp4")

if(cap.isOpened()):
    print("Video opened")
    while(cv2.waitKey(30) != ord('q')):
        ret,frame=cap.read()
        if ret==False:
            print("video ends")
            break

        cv2.imshow("Video",frame)


else:
    print("opening video failed")

cap.release()
cv2.destroyAllWindows()
