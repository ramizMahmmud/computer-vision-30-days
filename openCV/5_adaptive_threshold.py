import os
import cv2

path = os.path.join('.', 'images', 'hand_written.jpeg')
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
img = cv2.resize(img, (360, 640))
img_crop = img[20:470, 10:320]

# adaptive thresholding
th = cv2.adaptiveThreshold(img_crop,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,51,50)

cv2.imshow('crop', th)
cv2.waitKey(0)