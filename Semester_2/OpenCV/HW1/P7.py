"""
Draw a line starting from the left lower corner and ending in the right upper corner of the image
pic1.jpg. Display the original image and the changed one in separate windows.
"""

import cv2 as cv
import numpy as np


img = cv.imread('pic1.jpg')
cv.imshow('pic1', img)


#Drawing a line
#cv.line(img, point1, point2, color, thickness)

(h, w) = img.shape[:2] #w:image-width and h:image-height

cv.line(img, (w,0), (0, h), (0, 0, 255), thickness = 3)
cv.imshow('pic1_line', img)

cv.waitKey(0)

