'''
Beginnings of tennis ball detection with video
@author: Hayden Shively, sentex, Duncan Van Keulen
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    # This code shows a grayscale image, better for edge detection later on...
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # FIXME: Convert to HSV to look for the hue of the tennis ball
    blue = frame[:, :, 0]
    green = frame[:, :, 1]
    red = frame[:, :, 2]

    thresh = (green > 150).astype('uint8') * 255
    thresh[blue > 140] = 0
    thresh[red > 210] = 0

    cv2.imshow('thresh', thresh)
cap.release()
cv2.destroyAllWindows()