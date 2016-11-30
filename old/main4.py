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
    print high
    retval = algo1.run(imgOriginal, low, high, cv2.COLOR_BGR2HSV)
    if retval:
        (img, blur, center) = retval
        blur2 = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)
        #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img2 = np.concatenate((img, blur2), axis=1)
        cv2.imshow("Control", img2)
    else:
        img2 = np.concatenate((imgOriginal, imgOriginal), axis=1)
        cv2.imshow("Control", img2)
    
cv2.namedWindow("Control")
cv2.createTrackbar("Image", "Control", 0, 100, callback); #Hue (0 - 179)
#Create trackbars in "Control" window
cv2.createTrackbar("LowH", "Control", 1, 255, callback); #Hue (0 - 179)
cv2.createTrackbar("HighH", "Control", 9, 179, callback);

cv2.createTrackbar("LowS", "Control", 190, 254, callback); #Saturation (0 - 255)
cv2.createTrackbar("HighS", "Control", 254, 255, callback);

cv2.createTrackbar("LowV", "Control", 150, 254, callback);#Value (0 - 255)
cv2.createTrackbar("HighV", "Control", 254, 255, callback);

callback(0)
cv2.waitKey()
