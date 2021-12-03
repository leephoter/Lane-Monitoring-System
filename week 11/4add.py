import numpy as np
import cv2 as cv

img1 = cv.imread('256_flower.jpg')
img2 = cv.imread('256_love.jpg')
cv.imshow('256_flower', img1)
cv.imshow('256_love', img2)

px1 = img1[127, 134]
print(px1)
px2 = img1[127, 135]
print(px2)
px3 = px1 + px2
print(px3)
px4 = cv.add(px1, px2)
print(px4)

overlapImage = cv.addWeighted(img1, 0.2, img2, 0.7, -100.0)
cv.imshow('overlap', overlapImage)
cv.waitKey(0)
cv.destroyAllWindows()
