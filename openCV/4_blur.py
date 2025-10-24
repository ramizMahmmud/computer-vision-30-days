import os
import cv2

path =  os.path.join('.','images','unsplash_bird.jpg')

img = cv2.imread(path)

# Four blur function exists

# blur(img, (blureffect, blureffect))
#blureffect is an integer vlue which define the intensity of blur
# blureffect is the neigboring pixel size to average
# GausianBlur(img, (blureffect, blureffect), int)
# medianBlur(img, blureffect)

k_size = 7

img_blur = cv2.blur(img, (k_size, k_size))
img_gausian_blur = cv2.GaussianBlur(img, (k_size, k_size),5)
img_median_blur = cv2.medianBlur(img,k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_gausian_blur',img_gausian_blur)
cv2.imshow('img_median_blur',img_median_blur)
cv2.waitKey(0)
