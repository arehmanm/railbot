import cv2

# load the image
imgOriginal = cv2.imread("test.png")
#print type(imgOriginal)
count = 0
import math

def run(img, low, high, format):
    global count
    imgHSV = cv2.cvtColor(img, format); #Convert the captured frame from BGR to HSV
    imgThresholded = cv2.inRange(imgHSV, low, high); #Threshold the image
    #'''
    #morphological opening (remove small objects from the foreground)
    #imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)) );
    #imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) );
    
    #morphological closing (fill small holes in the foreground)
    #imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) );
    #imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) );
    #'''
    imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    #blur = cv2.medianBlur(imgThresholded, 5)
    #blur = cv2.dilate(blur, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    blur = imgThresholded.copy()
    blur2 = blur.copy()
    
    #cv2.imshow("Control", blur); #show the thresholded image
    #cv2.imshow("Original", imgOriginal); //show the original image
    vals = cv2.findContours(blur, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #print len(vals[1])
    if len(vals[1]) > 0:
        #for v in vals[1]:
            #if len(v) > 5:
                #e = cv2.fitEllipse(v)
                #cv2.ellipse(img, e, (0, 255, 0), 2)
                #x,y,w,h = cv2.boundingRect(v)
                #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


        def compare(a):
            if len(a) > 5:
                e1 = cv2.fitEllipse(a)
                #if e1[1][0] > 0:
                #    ratio = e1[1][1] / e1[1][0]
                #else:
                #    ratio = 0
                #print e1
                #print ratio
                # e1[2]
                return cv2.contourArea(a) * abs(math.cos(e1[2]*math.pi/180.0))
            else:
                return 0

        max_cont = max(vals[1], key=compare)
        #cv2.drawContours(img, vals[1], -1, (0,255,0), 2)
    
        mu = cv2.moments(max_cont, True);
        if mu['m00'] != 0:
            center = (int(mu['m10'] / mu['m00']), int(mu['m01'] / mu['m00']));
            #cv2.circle(img, center, 5, (255, 134, 100), 2);
            #x,y,w,h = cv2.boundingRect(max_cont)
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.imshow("Control", imgOriginal)
            #cv2.imshow("Control2", blur)
            #cv2.imwrite("output/thresh" + str(count) + ".png", blur2)
            #img2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            #cv2.imwrite("output/output" + str(count) + ".png", img2)
            count = count + 1
            return (img, blur2, center, max_cont)
    else:
        print "sorry, 0 m00"