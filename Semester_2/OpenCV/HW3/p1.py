"""
Open the image pic1.jpg and display it with the name pic1. Convert the image to the following
formats and display in separate windows: RGB, HSV, LAB, grayscale.
"""


# more advance concepts
# https://pythonwife.com/color-spaces-and-channels-in-opencv/

#how to switch between color spaces - a system of representing an array of pixel colors (rgb, gray scale, etc.)

import cv2 as cv
import numpy as np

img = cv.imread('pic1.jpg') 
cv.imshow('pic1', img)

#BGR - format used by opencv, similar to RGB but the bits are stored differently in the memory
#if we read an image with imread and then try to display with matplotlib, the pixel colors will be switched
#BGR is usually used on TVs, text is a bit blury compared to RGB

#Convert from bgr to rgb

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb) 

#Convert from bgr to hsv (hue, saturation, value), based on how humans see the color
#object recognition by color works

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv) 

#Convert from bgr to lab (l*a*b), washed down version
#Lab is a conversion of the same information as RGB or BGR to a lightness component L*, 
#and two color components - a*(colors from green to magenta) and b*(colors from blue to yellow)
#gives the same color across different devices

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 

#Converting an image from bgr to grayscale (grayscale - distribution of pixel intencities at different locations in your image)
#each pixel only carries the intencity information (the amount of light)

#why are grayscale images prefered in image processing?:
#-grayscale simplifies the algorithm and reduces computational requirements
#-colored images are also used, but often we combine color channels or do other operations to have more distinguished image featured

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

cv.waitKey(0)



