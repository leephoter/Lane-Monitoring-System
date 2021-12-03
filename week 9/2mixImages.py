import numpy as np
import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("512flower.jpg"))
if img is None:
    sys.exit("Could not read the image.")
print(img)
cv.imshow("512flower", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("512flower.jpg", img)

img2 = cv.imread(cv.samples.findFile("512rose.jpg"))
if img2 is None:
    sys.exit("Could not read the image.")
print(img2)
cv.imshow("512rose", img2)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("512rose.jpg", img2)

rose = img2[128:384, 128:384]
img[128:384, 128:384] = rose
cv.imshow("mixed", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("mixedFlower.jpg", img)
