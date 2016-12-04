# Standard imports
import cv2
from algos import algo1
from datetime import datetime

count = 0

def getCenter(img, low, high):
    global count
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite("output/output" + str(count) + ".png", img2)
    count = count + 1

    height, width, channels = img.shape
    #img = img[:, 0:width - 60]
    ret = algo1.run(img, low, high, cv2.COLOR_RGB2HSV)
    if ret:
        (image, blur, center, max_cnt) = ret
        x,y,w,h = cv2.boundingRect(max_cnt)
        #img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #cv2.imwrite("output/output" + str(count) + ".png", img2)
        #count = count + 1
        return (center, (x-w, y-h), (3*w, 3*h))

def getDiff(img1, img2):
    global count
    img3 = img2 - img1
    cv2.imwrite("output/img1_" + str(count) + ".png", img1)
    cv2.imwrite("output/img2_" + str(count) + ".png", img2)
    count = count + 1
