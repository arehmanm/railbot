# Standard imports 
import cv2
import numpy
import constants
from algos import algo1

low = constants.low_red
high = constants.high_red

def callback(val):
    n = cv2.getTrackbarPos('Image', 'Control')
    img1 = cv2.imread("../output/output" + str(8*n) + ".png")
    img2 = cv2.imread("../output/output" + str(8*n+1) + ".png")
    img3 = cv2.imread("../output/output" + str(8*n+3) + ".png")
    img8 = cv2.imread("../output/output" + str(8*n+7) + ".png")
    
    low = (cv2.getTrackbarPos('LowH', 'Control'), cv2.getTrackbarPos('LowS', 'Control'), cv2.getTrackbarPos('LowV', 'Control'))
    high = (cv2.getTrackbarPos('HighH', 'Control'), cv2.getTrackbarPos('HighS', 'Control'), cv2.getTrackbarPos('HighV', 'Control'))
    multiplier = cv2.getTrackbarPos('Mul', 'Control') / 2.0

    (img1, blur1, center1) = algo1.run(img1, low, high, cv2.COLOR_BGR2HSV)
    blur1 = cv2.cvtColor(blur1, cv2.COLOR_GRAY2BGR)
    cv2.circle(img1, center1, 5, (0, 255, 0), 2);
    imgc1 = cv2.add(img1, blur1)
    
    (img2, blur2, center2) = algo1.run(img2, low, high, cv2.COLOR_BGR2HSV)
    blur2 = cv2.cvtColor(blur2, cv2.COLOR_GRAY2BGR)
    offset = [q-p for (p, q) in zip(center1, center2)]
    center3 = (multiplier*offset[0]+center2[0], multiplier*offset[1]+center2[1])
    center3 = (int(center3[0]), int(center3[1]))
        
    cv2.circle(img2, center1, 5, (0, 255, 0), 2);
    cv2.circle(img2, center2, 5, (255, 150, 150), 2);
    cv2.circle(img2, center3, 5, (0, 255, 255), 2);
    imgc2 = cv2.add(img2, blur2)

    #cv2.circle(img3, center1, 5, (0, 255, 0), 2);
    #cv2.circle(img3, center2, 5, (255, 150, 150), 2);
    #cv2.circle(img3, center3, 5, (0, 255, 255), 2);
    imgc3 = cv2.add(img3, blur1, blur2)
    img = numpy.concatenate((imgc1, imgc2, imgc3, img8), axis=1)
    cv2.imshow("Control", img)
        #mouse.shoot(new_center, constants.screen, constants.window)
    
cv2.namedWindow("Control")
cv2.createTrackbar("Image", "Control", 1, 200, callback); #Hue (0 - 179)
cv2.createTrackbar("Mul", "Control", 5, 20, callback); #Hue (0 - 179)
#Create trackbars in "Control" window
cv2.createTrackbar("LowH", "Control", low[0], 255, callback); #Hue (0 - 179)
cv2.createTrackbar("HighH", "Control", high[0], 179, callback);

cv2.createTrackbar("LowS", "Control", low[1], 254, callback); #Saturation (0 - 255)
cv2.createTrackbar("HighS", "Control", high[1], 255, callback);

cv2.createTrackbar("LowV", "Control", low[2], 254, callback);#Value (0 - 255)
cv2.createTrackbar("HighV", "Control", high[2], 255, callback);

callback(0)
cv2.waitKey()
