#This code performs fire detection in an image using computer vision techniques. The input image is read using the cv2.imread function, and a 
#background subtraction algorithm (MOG2) is used to identify the foreground objects (i.e. the fire) in the image. The foreground mask is then 
#thresholded to produce a binary image, and morphological operations (closing with an elliptical kernel) are applied to remove noise and 
#fill in holes in the foreground objects. The contours of the resulting foreground objects are then extracted using the cv2.findContours function, 
#and a bounding box is drawn around each contour that meets a minimum area threshold (1000 pixels in this case). The resulting image is displayed
#using cv2.imshow and the windows are destroyed using cv2.destroyAllWindows.

import cv2
import numpy as np

image = cv2.imread("fireeeee.jpeg")

bg_subtractor = cv2.createBackgroundSubtractorMOG2()

fg_mask = bg_subtractor.apply(image)

_, fg_mask = cv2.threshold(fg_mask, 128, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:

    if cv2.contourArea(contour) < 1000:
        continue

    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Image", image)

cv2.destroyAllWindows()
