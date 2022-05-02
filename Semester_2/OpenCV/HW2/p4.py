"""
Open the image pic2.jpg and display it with the name pic2. Resize the image to have 2 times
bigger width and the same height as the original image, use INTER_AREA interpolation. Then
resize the original image to have 2 times smaller height and the same width as the original
image, use INTER_CUBIC interpolation. Display both versions in separate windows.
"""

import cv2 as cv

img = cv.imread('pic2.jpg') #3 channel image blue-green-red (bgr)

cv.imshow('pic2', img)

(h, w) = img.shape[:2] #w:image-width and h:image-height

#this interpolation method (or INTER_CUBIC - slower, but you get better quality) is useful when you are making your image smaller, INTER_AREA is useful when you are making the image larger
resize1 = cv.resize(img, (2*w, h), interpolation = cv.INTER_AREA) 
resize2 = cv.resize(img, (w, h//2), interpolation = cv.INTER_CUBIC) 
cv.imshow('Resize1', resize1)
cv.imshow('Resize2', resize2)

cv.waitKey(0)