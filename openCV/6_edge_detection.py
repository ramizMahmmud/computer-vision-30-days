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

# Laplacian Edge Detector
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Canny Edge Detector
#steps
# Noise Reduction
# Calculating the Intensity Gradient of the Image
# Suppression of False Edges
# Hysteresis Thresholding

blur = cv2.GaussianBlur(img, (5,5),1)
canny_img = cv2.Canny(img, threshold1=50,threshold2=150)
canny_blur = cv2.Canny(blur, threshold1=50, threshold2=200)
cv2.imshow('img_1',img_1)
cv2.imshow('Sobel', gradient_magnitude_sobel)
cv2.imshow('Laplacian',laplacian_abs)
cv2.imshow('Canny Blur', canny_blur)
cv2.imshow('Canny Image', canny_img)
cv2.imshow('Blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()