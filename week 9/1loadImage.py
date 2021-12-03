#  -*- coding: utf-8 -*- 

import cv2 as cv
import sys

img = cv.imread("512faces.jpg")
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Faces 512x512", img)

k = cv.waitKey(0)
