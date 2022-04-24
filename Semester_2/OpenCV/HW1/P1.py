"""
Open images pic1.jpg, pic2.jpg and pic3.jpg and display in separate windows with the names
pic1, pic2 and pic3 correspondingly.
"""

import cv2 as cv


#takes a path to an image and returns it as a matrix of pixels

img1 = cv.imread('pic1.jpg')
img2 = cv.imread('pic2.jpg')
img3 = cv.imread('pic3.jpg')

#displaying the image as a new window, passing the window name and the matrix of pixels to display

cv.imshow('pic1', img1) 
cv.imshow('pic2', img2) 
cv.imshow('pic3', img3) 

#a keyboard binding function, waits for a specific delay for a key to be pressed

cv.waitKey(0) #waits for an infinite amount of time for a keyboard key to be pressed
