import numpy as np
import cv2 as cv
import time

img = cv.imread('256_love.jpg')
img1 = np.copy(img)

cv.imshow("original", img)

for r in range(127, 137):
    for c in range(134, 144):
        img[r, c] = [0, 0, 255]
cv.imshow("pixelModified", img)

for r in range(0, 255):
    for c in range(0, 255):
        img1.itemset((r, c, 0), 255)
cv.imshow("colorModified", img1)

roi = img[155:175, 163:196]
img[177:197, 197:230] = roi
cv.imshow("regionAccess", img)

cv.waitKey(0)
cv.destroyAllWindows()
