"""
Open the image pic1.jpg and display it with the name pic1. Blur the image using Gaussian blur
using 2 different windows sizes: (3, 3) and (11, 11) and display both versions in separate
windows to compare with the original image
"""

import cv2 as cv

img = cv.imread('pic1.jpg') #3 channel image blue-green-red (bgr)

cv.imshow('pic1', img)

#2. Blur (can remove some of the noise in the image: bad lighting extra elements, camera sensor issues, etc.)
#many bluring techniques
#(3, 3) is the window size used during the blur, has to be an odd number - will talk about this later

blur3 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT) 
blur11 = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT) #more blur
cv.imshow('Blur3', blur3)
cv.imshow('Blur11', blur11)

cv.waitKey(0)