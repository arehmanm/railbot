# Standard imports
import cv2
import numpy as np
 
# load the image
imgOriginal = cv2.imread("../output/output0.png")
print type(imgOriginal)

def callback(val):
    n = cv2.getTrackbarPos('Image', 'Control')
    img1 = cv2.imread("../output/img1_" + str(n) + ".png")
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img1 = cv2.medianBlur(img1, 5)
    img2 = cv2.imread("../output/img2_" + str(n) + ".png")
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img2 = cv2.medianBlur(img2, 5)
    img3 = img2 - img1
    img = np.concatenate((img1, img2, img3), axis=1)
    cv2.imshow("Control", img)
    
cv2.namedWindow("Control")
cv2.createTrackbar("Image", "Control", 0, 100, callback); #Hue (0 - 179)
#Create trackbars in "Control" window
cv2.createTrackbar("LowH", "Control", 1, 255, callback); #Hue (0 - 179)
cv2.createTrackbar("HighH", "Control", 15, 179, callback);

cv2.createTrackbar("LowS", "Control", 190, 254, callback); #Saturation (0 - 255)
cv2.createTrackbar("HighS", "Control", 255, 255, callback);

cv2.createTrackbar("LowV", "Control", 150, 254, callback);#Value (0 - 255)
cv2.createTrackbar("HighV", "Control", 255, 255, callback);

callback(0)
cv2.waitKey()
