"""
Draw a red filled circle in the middle of the image pic2.jpg. Use an appropriate radius value so
that the whole circle is visible. Display the original image and the changed one in separate
windows.
"""

import cv2 as cv
import numpy as np


img = cv.imread('pic2.jpg')
cv.imshow('pic2', img)


#Drawing a circle
#cv.circle(img, center, radius, color, thickness)

(h, w) = img.shape[:2] #w:image-width and h:image-height

cv.circle(img, (w//2, h//2), np.min([w,h])//7, (0, 0, 255), thickness = -1)
cv.imshow('pic2_circle', img)

cv.waitKey(0)

