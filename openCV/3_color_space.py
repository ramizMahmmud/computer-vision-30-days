import os
import cv2

path = os.path.join('.','images','unsplash_bird.jpg')

img = cv2.imread(path)

#general form of image is bgr

#converting to rgb color space

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



cv2.imshow('img',img)
cv2.imshow('rgb', img_rgb)
cv2.imshow('gray',img_gray)
cv2.imshow('hsv',img_hsv)
cv2.waitKey(0)