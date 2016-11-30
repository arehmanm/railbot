# Standard imports
import cv2
from algos import algo1
from datetime import datetime

count = 0

def getCenter(img):
    global count
    height, width, channels = img.shape
    #img = img[:, 0:width - 60]
    low = (1, 159, 165)
    high = (9, 255, 255)
    ret = algo1.run(img, low, high, cv2.COLOR_RGB2HSV)
    if ret:
        (image, blur, center) = ret
        cv2.imwrite("output/output" + str(count) + ".png", image)
        count = count + 1
        return center

def getDiff(img1, img2):
    global count
    img3 = img2 - img1
    cv2.imwrite("output/img1_" + str(count) + ".png", img1)
    cv2.imwrite("output/img2_" + str(count) + ".png", img2)
    count = count + 1
