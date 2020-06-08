import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
    pass

#cap = cv.VideoCapture(1)
cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)
#uh = 40
#us = 255

while True:
    img = cv.imread('image.jpg')
    frame = cv.resize(img, (500,500))
    #_, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH" , "Tracking")
    l_s = cv.getTrackbarPos("LS" , "Tracking")
    l_v = cv.getTrackbarPos("LV" , "Tracking")
   
    u_h = cv.getTrackbarPos("UH" , "Tracking")
    u_s = cv.getTrackbarPos("US" , "Tracking")
    u_v = cv.getTrackbarPos("UV" , "Tracking")

    l_blk = np.array([l_h,l_s,l_v])
    u_blk = np.array([u_h,u_s,u_v])

    mask = cv.inRange(hsv, l_blk, u_blk)
    res = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    if cv.waitKey(1)& 0xFF == ord('q') :
        break
   

cv.waitKey(0)
cv.destroyAllWindows()
cap.release()




