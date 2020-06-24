import cv2 as cv
import numpy as np
import datetime

#function for line connecting and showing coordinates in the lines 
def click_event(event, x, y, flags,params):
    #event for clicking on objects and creating a line
    if event == cv.EVENT_LBUTTONDBLCLK: 
        cv.circle(img, (x,y), 3, (0,0,255), -1)
        print(x, ', ',y)
        font = cv.FONT_HERSHEY_SIMPLEX
        points.append((x,y))
        strXY = str(x) + ', '+str(y)
        cv.putText(img,strXY, (x,y), font, .5, (255,255,0),2)
        if len(points) >= 2:
            cv.line(img, points[-1], points[-2], (255,0,0), 5)
            cv.circle(img, (x,y), 3, (0,0,255), -1)
            strXY = str(x) + ', '+str(y)
            cv.putText(img,strXY, (x,y), font, .5, (255,255,0),2)
            cv.imshow('image', img)
    #event for coordinates in pictures
    if event == cv.EVENT_RBUTTONDBLCLK:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+str(green) + ', ' + str(red)
        cv.putText(img,strBGR, (x,y), font, .5, (255,255,0),2)
        cv.imshow('image', img)


#img = np.zeros((512,512, 3), np.uint8)

img = cv.imread("image.jpg")
#img = cv.resize(ims, (500,500))
cv.imshow('image', img)
points = []
cv.setMouseCallback('image',click_event)
cv.waitKey(0)
print(points)
cv.destroyAllWindows()

