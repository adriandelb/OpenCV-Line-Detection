import cv2 as cv
import numpy as np
import datetime

#Video Code
cap  = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 500)
#cap.set(4, 500)
#print(cap.get(3))
#print(cap.get(4))
fourcc = cv.VideoWriter_fourcc(*'XVID')
#out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))

print(cap.isOpened())

while(cap.isOpened()):
    ret, frame  = cap.read()
    if ret == True:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        datet  = str(datetime.datetime.now())
        frame = cv.putText(frame, datet, (10, 50), font, 1, (0,255,255),2, cv.LINE_AA)
        cv.imshow('frame', frame)
        if cv.waitKey(1)& 0xFF == ord('q'):
            break
    else:
        break
cap.release()
#out.release()
cv.destroyAllWindows() 
