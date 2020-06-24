import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time



def line_detection(cropped,frame):
    grey = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grey,(3,3),0)
    
    lineId = cv.inRange(blur, 0, 45)
   
    kernel = np.ones((3,3), np.uint8)
    lineId = cv.erode(lineId,kernel, iterations=1)
    lineId = cv.dilate(lineId,kernel, iterations=3)

    thresh = cv.adaptiveThreshold(lineId, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 17,2)
   

    contours_blk, hierarchy_blk = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    drawn = cv.drawContours(cropped,contours_blk,-1,(0,255,0), 2)
    return contours_blk, drawn





####################################################################################################

cap = cv.VideoCapture('video2.mov')
while cap.isOpened():    
    ret, frame = cap.read()
    cropped = frame[100:700, 1800:1920]
   
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
 
    contours_blk, drawn_contours = line_detection(cropped, frame)
    #print(len(contours_blk))
    
    if len(contours_blk) > 0:
        blackbox = cv.minAreaRect(contours_blk[0])
        print(contours_blk[0])
        (x_min, y_min), (w_min, h_min), ang = blackbox
        if ang < -45 :
            ang = 90 + ang
        if w_min < h_min and ang > 0:
            ang = (90-ang)*-1
        if w_min > h_min and ang < 0:
            ang = 90 + ang
        setpoint = 320
        error = int(x_min - setpoint)
        ang = int(ang)
        box = cv.boxPoints(blackbox)
        box = np.int0(box)
        cv.drawContours(drawn_contours,[box],0,(0,0,255),3)

    
    #######################
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

#####################################################################################################
cap.release()
cv.destroyAllWindows()