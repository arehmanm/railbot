import cv2

# load the image
imgOriginal = cv2.imread("test.png")
print type(imgOriginal)
count = 0

def run(img, low, high, format):
    global count
    imgHSV = cv2.cvtColor(img, format); #Convert the captured frame from BGR to HSV
    imgThresholded = cv2.inRange(imgHSV, low, high); #Threshold the image
    '''   
    #morphological opening (remove small objects from the foreground)
    cv2.erode(imgThresholded, imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) );
    cv2.dilate(imgThresholded, imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) ); 
    
    #morphological closing (fill small holes in the foreground)
    cv2.dilate(imgThresholded, imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) ); 
    cv2.erode(imgThresholded, imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) );
    #'''
    blur = cv2.medianBlur(imgThresholded, 5)
    #blur2 = blur.copy()
    
    #cv2.imshow("Control", blur); #show the thresholded image
    #cv2.imshow("Original", imgOriginal); //show the original image
    vals = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print len(vals[1])
    if len(vals[1]) > 0:
        max_cont = max(vals[1], key=cv2.contourArea)
        #cv2.drawContours(img, vals[1], -1, (0,255,0), 2)
    
        mu = cv2.moments(max_cont, True);
        if mu['m00'] != 0:
            center = (int(mu['m10'] / mu['m00']), int(mu['m01'] / mu['m00']));
            cv2.circle(img, center, 5, (255, 134, 100), 2);
            #cv2.imshow("Control", imgOriginal)
            #cv2.imshow("Control2", blur)
            #cv2.imwrite("output/thresh" + str(count) + ".png", blur2)
            #img2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            #cv2.imwrite("output/output" + str(count) + ".png", img2)
            count = count + 1
            return (img, blur, center)
    else:
        print "sorry, 0 m00"