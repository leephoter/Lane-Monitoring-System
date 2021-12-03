'''
Gray -> Threshold-> Canny -> HoughLine

'''
import cv2 as cv
import numpy as np
from doImage import *
from math import *

fileName = 'straight22'

img = cv.imread(fileName+'.jpg')

# Gray
imgGray = cv.imread(fileName+'.jpg', 0)

# Threshold
ret, thresh = cv.threshold(imgGray, 200, 255, cv.THRESH_BINARY)
myShow(fileName+'_thresh', thresh)

# Canny
edges = cv.Canny(thresh, 50, 350)
myShow(fileName+'_Canny', edges)

# Hough Line
lines = cv.HoughLines(edges, 1, np.pi/180, 85)

imgHough = np.copy(img)
for line in lines:
    rho, theta = line[0]
    myDrawLine(rho, theta, imgHough, (0, 0, 255), 1)
myShow(fileName+'_Hough', imgHough)
