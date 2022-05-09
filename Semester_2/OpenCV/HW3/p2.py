"""
Open the image pic1.jpg and display it with the name pic1. Separate the image into its 3
channels. Display both the colored and grayscale versions of each channel in separate
windows.
"""



#Splitting and merging color channels
#color image consists of multiple channels (red green blue), these 3 color channels merged together
#We can split an image into blue, green and red components
#e.g. is one channel has better quality than the other - can be used to shapen the overall imange


import cv2 as cv
import numpy as np

img = cv.imread('pic1.jpg') 
cv.imshow('pic1', img) 

b, g, r = cv.split(img)

#displayed as grayscale images, which shows the distribution of pixel intancities
#white regions - more concentration of pixel values, darker regions - little or no pixels of that color in that region
cv.imshow('gray_blue', b)
cv.imshow('gray_green', g)
cv.imshow('gray_red', r)

#an additional way of looking at the color instead of grayscale
#reconstructing the image for this

#creating a blank image using numpy
#'uint8' is for images
#the blank image consists of height and width, so by merging the blue image and its respective compartment, we are setting the green and red components to blank and displaying only the blue component, same for green and red

blank = np.zeros(img.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

#now we can visualize the distribution of pixel intensities much better
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)

