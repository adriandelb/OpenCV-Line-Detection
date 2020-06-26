import cv2 as cv
import os 
import numpy as np
import matplotlib.pyplot as plt
import time


####################################################################################################
############################### Function Definitions ###############################################
####################################################################################################

#function for line detection
def line_detection(cropped,frame):
    #Local Variables
    filterSize = (3,3)
    maxPixelValue = 45
    minPixelValue = 0
    kernel = np.ones(filterSize, np.uint8)

    #convert rgb to greyscale
    grey = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)

    #blur image to reduce noise for analysis (The (3,3) is the kernal size, the- 
    # bigger the filter the more the pixels are combined together)
    blur = cv.GaussianBlur(grey,filterSize,0)

    #creates a range for acceptable pixel values (This value is changed depending- 
    #on the intensity of pixel range. [image, lowerbound, Upperbound])
    lineId = cv.inRange(blur, minPixelValue, maxPixelValue)
   
    #erode the line to limit noise near the edges. It brings in the edge. Iteration is- 
    #the number of times it is run. No more times it runs, the more it is eroded but costs performance
    lineId = cv.erode(lineId,kernel, iterations=1)
    #expands 
    lineId = cv.dilate(lineId,kernel, iterations=3)

    thresh = cv.adaptiveThreshold(lineId, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 17,2)
   
    contours_blk, hierarchy_blk = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    drawn = cv.drawContours(cropped,contours_blk,-1,(0,255,0), 2)
    return contours_blk, drawn



####################################################################################################
############################### Main Program #######################################################
####################################################################################################


#path for video file
path = 'C://users/adelbosque/Documents/Assignments/OpenCV-Line-Detection/videos/video2.mov'
#opens video file under path
cap = cv.VideoCapture(path)


#loop that runs program with the video is running
while cap.isOpened():    
    #reads each frame in cap and stores it in frame
    ret, frame = cap.read()

    #check statement
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

  
    #crop the original frame size for analysis
    cropped = frame[100:700, 1800:1920]

    #function call for detecting the line. Function returns an array of contours and draws the contours on the image
    contours_blk, drawn_contours = line_detection(cropped, frame)
    ##############################################################
    

    if len(contours_blk) > 0:
        blackbox = cv.minAreaRect(contours_blk[0])
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