"""
Draw an orange rectangle with thickness 2 on the image pic2.jpg. Use appropriate measures
for the rectangle so that the whole rectangle is visible. Display the original image and the
changed one in separate windows.
"""

import cv2 as cv
import numpy as np


img = cv.imread('pic2.jpg')
cv.imshow('pic2', img)


#Drawing a rectangle
#cv.rectangle(img, point1, point2, color, thickness)

(h, w) = img.shape[:2] #w:image-width and h:image-height

cv.rectangle(img, (w//8, h//8), (w//3, h//3), (0, 128, 255), thickness = 2)
cv.imshow('pic2_rectangle', img)

cv.waitKey(0)

