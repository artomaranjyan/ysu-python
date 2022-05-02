"""
Open the image pic1.jpg and display it with the name pic1. Convert the image to grayscale and
display in a separate window to compare with the original image.
"""

import cv2 as cv

img = cv.imread('pic1.jpg') #3 channel image blue-green-red (bgr)

cv.imshow('pic1', img)

# 1. Converting to grayscale (distribution of pixels rather than the color itself)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('pic1_gray', gray)

cv.waitKey(0)