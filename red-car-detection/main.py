import os
import cv2
from PIL import Image

from color import get_range

red = [0, 0, 255] # red color in BGR colorspace
path = os.path.join('.', 'video.mp4')
video = cv2.VideoCapture(path)

ret = True

while ret:
    ret, frame = video.read()
    if ret:
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lowerLimit, upperLimit = get_range(color=red)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame =cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0), 7)
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()