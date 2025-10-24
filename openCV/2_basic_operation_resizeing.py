import os
import cv2

path = os.path.join('.','images','unsplash_bird.jpg')

# read image

img = cv2.imread(path)

# After watching shape of the image, we can modify image shape
# In shape (height, width, number of channel)

# to resize image cv2.resize(name-of-file, (with, height))


#in this example image shape: (183, 275, 3)

resized_image = cv2.resize(img, (200,100))
print(img.shape)
print(resized_image.shape)


#visualize image

cv2.imshow('image',img)
cv2.imshow('resized_image', resized_image)
cv2.waitKey(0)