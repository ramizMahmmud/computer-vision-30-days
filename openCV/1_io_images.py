import cv2
import os
#image path
img_path = os.path.join('.','images','unsplash_bird.jpg')

# read image
img = cv2.imread(img_path)

# write image
cv2.imwrite(os.path.join('.','images','bird_out.jpg'),img)

# visualize image
cv2.imshow('image',img)
cv2.waitKey(0)