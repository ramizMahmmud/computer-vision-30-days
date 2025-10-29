import os
import cv2

path = os.path.join('.', 'images', 'objects.png')
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 190, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    print(cv2.contourArea(cnt))
    if cv2.contourArea(cnt) > 5000:
       # cv2.drawContours(img, cnt, -1, (0, 255, 0),2)
        
        # creating box around obects
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x1, y1), (x1+w, y1 + h), (0, 255, 0),2)
        
        

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()