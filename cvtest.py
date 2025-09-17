import cv2
import numpy as np


img = cv2.imread('images/Stop_sign.png')
img = cv2.resize(img, (200, 200))

cv2.imshow('image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#cv2.imshow('image HSV', img)

red_mask = cv2.inRange(img, (0, 100, 100), (10, 255, 255))
white_mask = cv2.inRange(img, (0, 0, 200), (255, 30, 255))

cv2.imshow('red mask', red_mask)
cv2.imshow('white mask', white_mask)

img_mask = cv2.bitwise_and(img, img, mask=red_mask)
cv2.imshow('image mask', img_mask)
img_mask_2 = cv2.bitwise_and(img, img, mask=white_mask)
cv2.imshow('image mask 2', img_mask_2)

cv2.waitKey(0)

cv2.destroyAllWindows()