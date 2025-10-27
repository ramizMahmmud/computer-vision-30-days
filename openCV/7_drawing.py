
import os
import cv2


path = os.path.join('.', 'images', 'whiteboard.webp')

img = cv2.imread(path)

# drawing argument: source image, coordinate, color, thickness
print(img.shape)
#line
cv2.line(img,(35, 35), (70, 70), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (40, 100), (100, 150), (0, 0, 255), -1) #fills inside

# circle
cv2.circle(img, (200, 100), 20, (255, 0, 0), 7)

# text

cv2.putText(img, 'Hello World!', (150, 200), cv2.FONT_HERSHEY_PLAIN, 2, (0, 25, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
