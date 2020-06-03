import cv2 as cv
import numpy as np


img = cv.imread('picture.jpg')
ims = cv.resize(img, (500,500))
print(ims.shape)
print(ims.size)
print(ims.dtype)

b,g,r = cv.split(ims)
ims = cv.merge((b,g,r))

dot = ims[189:179, 274:235]
ims [205:179, 290:235] = dot

cv.imshow('image', ims)
cv.waitKey(0)
cv.destroyAllWindows()




