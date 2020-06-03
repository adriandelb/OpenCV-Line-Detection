import cv2 as cv

cap  = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))

print(cap.isOpened())

while(cap.isOpened()):
    ret, frame  = cap.read()
    if ret == True:
        out.write(frame)
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', grey)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()