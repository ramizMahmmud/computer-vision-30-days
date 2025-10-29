import os
import cv2
import numpy as np
from color import get_range

red = [0, 0, 255] # red color in BGR colorspace
path = os.path.join('.', 'video.mp4')
video = cv2.VideoCapture(path)

ret = True

while ret:
    ret, frame = video.read()
    if ret:
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red_upper = np.array([180, 255, 255], np.uint8)
        red_lower = np.array([136, 87, 111], np.uint8)
        mask = cv2.inRange(hsvImage, red_lower, red_upper)
        contour, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contour:
            if cv2.contourArea(cnt)>1000:
                x1, y1, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x1, y1), (x1+w, y1+h),(0,255,0),5)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
video.release()
cv2.destroyAllWindows()


