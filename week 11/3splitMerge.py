import numpy as np
import cv2 as cv
import time

img = cv.imread('256_love.jpg')
cv.imshow("original", img)

bImg, gImg, rImg = cv.split(img)

cv.imshow("blueImage", img[:, :, 0])
cv.imshow("greenImage", gImg)
cv.imshow("redImage", rImg)

mergedImg = cv.merge((bImg, gImg, rImg))
cv.imshow("merged", mergedImg)

cv.waitKey(0)
cv.destroyAllWindows()
