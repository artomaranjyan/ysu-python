"""
Open the image pic2.jpg and display it with the name pic2. Blur the picture using average and
bilateral blurring methods and display in separate windows. (For the parameters, use the values
of your choice). Write a short comment if you see any particular difference when using different
parameter values for the second method and comparing it to the averaging method.
"""


#Smoothing and bluring images 

#We usually blur an image when it has a lot of noise, noise that's caused from camera sensors or lighting when the image was taken. We will reduce some of that noise by using bluring techniques. We have seen Gaussian blur already, there are some other techniques that we will look at.

#Concepts
#What happens when we try to apply a blur.
#The first thing we need to define is kernel (or window) - a window that you draw over a specific portion of an image and something happens to the pixels of that window. This window has a size, which is called a kernel size (num of rows and num of cols: say, 3x3). 
#The blur is applied to the middle pixel as a result of surrounding pixels (3x3 case)

#Bluring methods


import cv2 as cv
import numpy as np

img = cv.imread('pic2.jpg') 
cv.imshow('pic2', img)

#Averaging

#pixel intencity of the middle pixel of the kernel will be computed as an everage of pixel intencity of surrounding pixels in the kernel
#Then the kernel window slides to the right until the end of the image and then down, computing this for all image pixels

average = cv.blur(img, (3,3))
cv.imshow('average blur', average)


#Bilateral blur

#The most effective, used in advanced computer vision projects. In this case even though the image is blured, the edges of the image are retained. 

bilateral = cv.bilateralFilter(img, 5, 15, 15)  #img, diameter, sigmacolor (larger value means more colors in the neighbourhood will be considered when the blur is computed), sigmaSpace (larger values means that pixels further out of the center pixel will influence the bluring calculation)

#looks really similar to the original image when we have a small diameter, when we increase the diameter and the other 2 parameters we see the difference
cv.imshow('bilateral', bilateral)

cv.waitKey(0)


