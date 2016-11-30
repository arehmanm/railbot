# Standard imports
import cv2
import numpy as np;
 
# load the image
image = cv2.imread("test.png")

# define the list of boundaries
boundaries = [
    ([0, 0, 200], [255, 255, 255])
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY);
    gray = cv2.medianBlur(gray, 5)
    
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 20
    
    params.filterByInertia = True
    params.maxInertiaRatio = 0.4
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create(params)
     
    # Detect blobs.
    keypoints = detector.detect(gray)
     
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
     
    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)