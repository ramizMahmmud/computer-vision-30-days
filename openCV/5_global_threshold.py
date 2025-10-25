import os
import cv2


img_path_lion = os.path.join('.','images','raccon.jpg')
# read image

img_raccon = cv2.imread(img_path_lion)

# gray_image

gray_raccon = cv2.cvtColor(img_raccon,cv2.COLOR_BGR2GRAY)

# resize
gray_raccon_resized = cv2.resize(gray_raccon, (365, 578))


# threshold (source_image, threshold_number correspnding to zero(white), maximum pixel, threshold function)


ret_raccon_resized, thres_raccon_resized = cv2.threshold(gray_raccon_resized, 80, 255, cv2.THRESH_BINARY)

# to clean nois blur function can be used
thresh = cv2.blur(thres_raccon_resized, (7,7))

ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)



cv2.imshow('gray_raccon',gray_raccon_resized)
cv2.imshow('thres_raccon_resized',thres_raccon_resized)
cv2.imshow('blur_thresh', thresh)
cv2.waitKey(0)
