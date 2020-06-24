import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

 

def setup():
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv.CAP_PROP_FPS, 40)    

def calibration():
    #take screenshot and calibrate image
    print("entered")


def check_Video():
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")

def grab_frame():
    print(index)
    frame = inF[index]
    return cv.cvtColor

index = 0
cap = cv.VideoCapture('video.MOV') 
video []
check_Video()
#cv.namedWindow("Guassian Blured",cv.WINDOW_NORMAL )

title = ['Origial Video', 'Gausian Blur']
while cap.isOpened():
    
    ret, frame = cap.read()
    setup()
    #edge = cv.Canny(frame. )
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.imshow()
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()