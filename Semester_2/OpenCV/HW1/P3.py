"""
Rescale the image pic1.jpg by 0.5 and display the original image and the rescaled one in
separate windows

We usually do this to prevent using too much of computational power

Rescaling - modifying height and width to a perticular height and width

best practice - downscale, or change height and width to a smaller values rather than larger
"""

import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #will talk more about this later

img = cv.imread('pic1.jpg')

img_rescaled = rescaleFrame(img, 0.5)

cv.imshow('pic1', img)
cv.imshow('pic1_rescaled', img_rescaled)


cv.waitKey(0)


