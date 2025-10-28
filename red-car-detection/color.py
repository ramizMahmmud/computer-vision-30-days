import numpy as np
import cv2

def get_range(color):
    c = np.uint8([[color]]) #bgr values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    hue = hsvC[0][0][0] # get the hue value of object
    # Handle red hue wrap-around
    if hue >= 165: #upper limit for divided red hue
        lowerLimit = np.array([hue -10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15: # lower limit for divided red hue
        lowerLimit = np.array([0, 100,100], dtype=np.uint8)
        upperLimit = np.array([hue+10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue-10,100,100], dtype=np.unit8)
        upperLimit = np.array([hue+100, 255, 255], dtype=np.uint8)
    return lowerLimit, upperLimit
        