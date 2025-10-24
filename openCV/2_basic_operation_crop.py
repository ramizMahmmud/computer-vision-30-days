import os
import cv2

path = os.path.join('.','images', 'unsplash_bird.jpg')

img = cv2.imread(path)

print(img.shape)

#image is an numpy array
# to crop an image use array indexing

cropped_img = img[10:175, 100:250]
cv2.imshow('img',img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)