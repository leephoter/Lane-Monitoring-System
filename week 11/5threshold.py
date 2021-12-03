import cv2 as cv
import numpy as np

img = cv.imread('256_love.jpg', 0)

ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh11 = cv.threshold(img, 10, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow('Original', img)
cv.imshow('BINARY', thresh1)
cv.imshow('BINARY_INV', thresh2)
cv.imshow('TRUNC', thresh3)
cv.imshow('TOZERO', thresh4)
cv.imshow('TOZERO_INV', thresh5)
cv.imshow('BINARY1', thresh11)
cv.waitKey(0)
cv.destroyAllWindows()
