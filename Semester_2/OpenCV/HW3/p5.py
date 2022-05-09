#4 basic bitwise operators - AND, OR, XOR, NOT
#Used a lot in computer vision, especially when using masks
#Pixels are turned on and off depending if they have a value of 1 or 0

import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype = 'uint8')

#We will use this blank variable as a basis to draw a rectangle and a circle

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 150, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 150, -1)


#Bitwise XOR

bitwise_xor = cv.bitwise_xor(rectangle, circle)

#returns only non-intersecting regions of 2 images 
cv.imshow('1', bitwise_xor) 

#Bitwise OR

bitwise_or = cv.bitwise_or(rectangle, circle)

#returns both intersecting and non-intersecting regions of 2 images 
cv.imshow('2', bitwise_or) 

blank = np.zeros((400, 400, 3), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (147, 20, 255), -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (147, 20, 255), -1)

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('3', bitwise_xor) 

cv.waitKey(0)

