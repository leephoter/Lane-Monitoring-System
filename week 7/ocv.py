import numpy as np
import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("256_flower.jpg"))
if img is None:
    sys.exit("Could not read the image.")
print(img)
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("256_flower.jpg", img)

img2 = cv.imread(cv.samples.findFile("256_rose.jpg"))
if img2 is None:
    sys.exit("Could not read the image.")
print(img2)
cv.imshow("Display window", img2)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("256_rose.jpg", img2)

rose = img2[64:192, 64:192]
img[64:192, 64:192] = rose
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("korea.jpg", img)
