import cv2
import RPi.GPIO as gp

def capture():
    cam = cv2.VideoCapture(0,cv2.CAP_V4L)

    cam.set(3,256) # w
    cam.set(4,256) # h
    gp.setmode(gp.BCM)
    gp.setwarnings(False)
    gp.setup(17,gp.IN) 


    while(True) :
        ret, frame = cam.read()

        cv2.imshow('Video Test',frame)

        if gp.input(17) == 0:
            break
        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return frame