'''
A script that can detect the color of a tennis ball
@author Hayden Shively
'''


import cv2
# import numpy as np

image = cv2.pyrDown(cv2.pyrDown(cv2.imread('tennisball3.jpg')))  # Change to tennisball/2/3/4 and see what happens
cv2.imshow('source', image)

blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]

thresh = (green > 150).astype('uint8')*255
thresh[blue > 140] = 0
thresh[red > 210] = 0

cv2.imshow('thresh',thresh)
cv2.waitKey(0)