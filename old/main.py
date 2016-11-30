# import the necessary packages
import numpy as np
import cv2

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
    
    mu = cv2.moments(gray, True);
    print mu
    center = (int(mu['m10'] / mu['m00']), int(mu['m01'] / mu['m00']));
    print center
    
    res = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR);

    cv2.circle(res, center, 10, (0, 0, 255));

    cv2.imshow("Result", res);
    cv2.waitKey();
    
    # show the images
    #cv2.imshow("images", output)
    #cv2.waitKey(0)