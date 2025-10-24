import os
import cv2

path = os.path.join('.','videos','228847_tiny.mp4')

#read
video = cv2.VideoCapture(path)

#visualize

ret = True

while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(33)


# cleaning memory
video.release()
cv2.destroyAllWindows()
    