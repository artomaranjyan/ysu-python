"""
Open the image pic3.jpg and display it with the name pic3. Find the edges of the image using
Canny edge detector and then try to find its contours with parameters of your choice. Then
convert the original image to grayscale and try to find the contours on a blurred version of the
grayscale of the original image. Display the 2 results in separate windows to compare.
"""


#countours - boundaries of objects
#line created by joining the boundary points of an object
#countours are different from edges from a mathematical point of view

#useful tools for shape analysis, object detection and recognition 

#step1 - convert to grayscale
#step2 - canny edge detector
#step3 - contours
#step4 - try a blur
#step5 - thresholding the image
 
import cv2 as cv
import numpy as np

img = cv.imread('pic3.jpg') 
cv.imshow('pic3', img) 

canny = cv.Canny(img, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 
# takes edges (canny), mode - RETR_EXTERNAL (only external edges), RETR_LIST (all the contours), etc.; contour approximation method - CHAIN_APPROX_NONE just returns all contours, CHAIN_APPROX_SIMPLE - compresses all contours, e.g. if the contour is a line, we don't get all points, just the endpoints VS CHAIN_APPROX_NONE gives all line points
# returns contours (list) and hierarchies (refers to hierarchical representation of contours used, won't go into details)


#visualizing the detected contours on the image
blank = np.zeros(img.shape, dtype = 'uint8')

#drawing contours on the blank image
cv.drawContours(blank, contours, -1, (0, 0, 255), 1) #image to draw over, contours list, contour index (-1 - all contours), color, thickness

cv.imshow('contours drawn (canny)', blank)


#trying on the blur

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)

contours, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

blank = np.zeros(img.shape, dtype = 'uint8')

#drawing contours on the blank image

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) #image to draw over, contours list, contour index (-1 - all contours), color, thickness

cv.imshow('contours drawn (blur)', blank)

cv.waitKey(0)