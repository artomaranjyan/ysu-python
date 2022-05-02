"""
Open the image pic2.jpg and display it with the name pic2. Translate the image to go down by
100 pixels and to the right by 50 pixels. Then rotate the image around its center by 50 degrees.
Then flip the resulting image both vertically and horizontally. Display the result after each action
in a separate window.
"""


import cv2 as cv
import numpy as np

img = cv.imread('pic2.jpg') 

cv.imshow('pic2', img)

# Translation - shifting an image along x and y axes (up, down, right, left)
def translate(img, x, y): #image, # of pixels you want to shift in x and y axes
    #-x --> left
    #-y --> up
    #x --> right
    #y --> down
    
    transMat = np.float32([[1, 0, x], [0, 1, y]]) #translation matrix
    dimensions = (img.shape[1], img.shape[0]) #(width, height)
    
    return cv.warpAffine(img, transMat, dimensions)

img = translate(img, 50, 100) #right by 50 pixels and down by 100 pixels    
cv.imshow('Translated', img)


# Rotation - specify a rotation point to shift image around that point
def rotate(img, angle, rotPoint = None): #assume that None - rotating around the center
    
    (height, width) = img.shape[:2]
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 - scale
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)


img = rotate(img, 50)
cv.imshow('Rotated', img)


#Flipping
#flipcode - 0, 1 or -1; 0 - vertical flip (over the x axes), 1 - horizontal flip (over the y axes), -1 - both vertically and horizontally
img = cv.flip(img, 0)
cv.imshow('Vertically flipped', img)

img = cv.flip(img, 1)
cv.imshow('Horizontally flipped', img)

cv.waitKey(0)
