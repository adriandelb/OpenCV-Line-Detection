import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

'''
def blacklineDetection(frame, kernal):
    line = cv.inRange(frame, (0,0,0), (0,0,50))
    line = cv2.erode(Blackline, kernel, iterations=5)
	line = cv2.dilate(Blackline, kernel, iterations=9)
return line
'''
def imag_pro(frame):
    kernel = np.ones((2,2), np.uint8)
    lineId = cv.inRange(frame, (0,0,0), (50,25,25))
    lineId = cv.erode(lineId,kernel, iterations=1)
    lineId = cv.dilate(lineId,kernel, iterations=1)
    lineId = cv.GaussianBlur(lineId,(5,5),0)
    return lineId

currentframes = 0
kernel_size = 3
scale = 1
delta = 0
ddepth = cv.CV_16S

cap = cv.VideoCapture('video.mov')

while cap.isOpened():    
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    blur = cv.GaussianBlur(frame,(5,5),0)

    grey = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    grey = cv.Laplacian(grey,cv.CV_16S)
  #  low_color = np.array([0,0,0])
   # upper_color = np.array([45,45,45])
    lineId = cv.inRange(grey, 0, 40)

   # kernel = np.ones((2,2), np.uint8)
    #lineId = cv.erode(lineId,kernel, iterations=1)
    #lineId = cv.dilate(lineId,kernel, iterations=2)

    #lineId = cv.GaussianBlur(lineId,(5,5),0)
  #  lineId = cv.adaptiveThreshold(lineId, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 17)
    contours_blk, hierarchy_blk = cv.findContours(lineId.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame,contours_blk,-1,(0,255,0), 3)
    

  

    #######################
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()