import os
import cv2

path = os.path.join('.', 'images', 'unsplash_bird.jpg')

img_1 = cv2.imread(path)
img = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
# Sobel operatior
# apply sobel operatior
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=1)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=1)
# compute gradient magnitude
gradient_magnitude_sobel = cv2.magnitude(sobelx, sobely)
#convert to unit8
gradient_magnitude_sobel = cv2.convertScaleAbs(gradient_magnitude_sobel)

# Laplacian 
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian_abs = cv2.convertScaleAbs(laplacian)

cv2.imshow('img_1',img_1)
cv2.imshow('Sobel', gradient_magnitude_sobel)
cv2.imshow('Laplacian',laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()