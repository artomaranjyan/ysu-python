"""
Open the image pic2.jpg and display it with the name pic2. Apply the correct method so that
only a circle of radius of 70 pixels is left right in the middle of the picture. 
"""


#We can perform masking using bitwise operations
#Masking allows to focus on particular parts of the image instead of the whole image
#e.g. image of people and you are interested in faces only, you apply masks over faces and remove the rest

import cv2 as cv
import numpy as np


img = cv.imread('pic2.jpg') 
cv.imshow('pic2', img) 


#dimentions of the mask have to be the same as those of the image
blank = np.zeros(img.shape[:2], dtype = 'uint8')

#we will create a circular mask, drawing a circle over the blank image

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 70, 255, -1)

masked_image = cv.bitwise_and(img, img, mask=mask)

cv.imshow('masked with circle', masked_image) 

cv.waitKey(0)

