# Standard imports
import cv2
import numpy as np
from algos import algo1

def callback(val):
    n = cv2.getTrackbarPos('Image', 'Control')
    imgOriginal = cv2.imread("../output/output" + str(n) + ".png")
    
    low = (cv2.getTrackbarPos('LowH', 'Control'), cv2.getTrackbarPos('LowS', 'Control'), cv2.getTrackbarPos('LowV', 'Control'))
    high = (cv2.getTrackbarPos('HighH', 'Control'), cv2.getTrackbarPos('HighS', 'Control'), cv2.getTrackbarPos('HighV', 'Control'))
    print low
    (img, blur, center) = algo1.run(imgOriginal, low, high, cv2.COLOR_BGR2HSV)
    cv2.imshow("Control", img)
    
cv2.namedWindow("Control")
cv2.createTrackbar("Image", "Control", 0, 50, callback); #Hue (0 - 179)
#Create trackbars in "Control" window
cv2.createTrackbar("LowH", "Control", 1, 255, callback); #Hue (0 - 179)
cv2.createTrackbar("HighH", "Control", 9, 179, callback);

cv2.createTrackbar("LowS", "Control", 159, 255, callback); #Saturation (0 - 255)
cv2.createTrackbar("HighS", "Control", 255, 255, callback);

cv2.createTrackbar("LowV", "Control", 165, 255, callback);#Value (0 - 255)
cv2.createTrackbar("HighV", "Control", 255, 255, callback);

callback(0)
cv2.waitKey()
