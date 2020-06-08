import cv2 as cv
import numpy as np

img  = cv.imread('picture.jpg',0)
#frame = cv.resize(img, (500,500))
th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 17)
ret3, th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("th2", th2)



cv.waitKey(0)
cv.destroyAllWindows()





