import numpy as np
import cv2 as cv
import time

img = cv.imread('512love.jpg')
grayImg = cv.imread('512love.jpg', 0)

# print(img.shape)
rowSize, colSize, channels = img.shape
print("rowSize:%d colSize:%d channels:%d" % (rowSize, colSize, channels))
print("img.size : %d" % (img.size))
print(img.dtype)

cv.imshow("gray", grayImg)
cv.imshow("color", img)

img[:, :, 2] = 0
cv.imshow("result", img)

cv.waitKey(0)
cv.destroyAllWindows()
