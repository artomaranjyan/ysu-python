"""
Open the image pic2.jpg and display it with the name pic2. Try to detect the image edges using
Canny edge detector and display the result in a separate window. Then run the edge detector
on a blurred version of an image (use a window size of your choice) and display the result in a
different window to compare.
"""

import cv2 as cv

img = cv.imread('pic2.jpg') #3 channel image blue-green-red (bgr)

cv.imshow('pic2', img)

#Edge Cascade - trying to find the edges present in the image
#many versions available
#125 and 175 are threshold values

canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)
#we can reduce the number of edges by using bluring
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Edges_blured', canny)

cv.waitKey(0)