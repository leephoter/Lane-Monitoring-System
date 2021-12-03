'''
Gray -> ROI -> Threshold-> Canny -> HoughLine

'''
import cv2 as cv
import numpy as np
from doImage import *
from math import *

fileName = 'straight22'

img = cv.imread(fileName+'.jpg')

# Gray
imgGray = cv.imread(fileName+'.jpg', 0)
imgRoi = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
imgOut = np.zeros(img.shape, np.uint8)

# Region Of Interest
syROI = 252
eyROI = 369
pointRoi = np.array([[280, 200], [80, 350], [550, 350], [350, 200]], np.int32)
cv.fillConvexPoly(imgRoi, pointRoi, 255)
imgRoiDisp = cv.addWeighted(imgGray, 0.8, imgRoi, 0.2, 0)
myShow(fileName+'_Roi', imgRoiDisp)

# Threshold
ret, thresh = cv.threshold(imgGray, 200, 255, cv.THRESH_BINARY)
# myShow(fileName+'_Thresh', thresh)
for r in range(0, img.shape[0]):
    for c in range(0, img.shape[1]):
        if(imgRoi[r, c] == 0):
            thresh[r, c] = 0
# myShow(fileName+'_roiThresh', thresh)

# Canny
edges = cv.Canny(thresh, 50, 350)
# myShow(fileName+'_Canny', edges)

# Hough Line
lines = cv.HoughLines(edges, 1, np.pi/200, 53)  # 30, 20

imgHough = np.copy(img)
for line in lines:
    rho, theta = line[0]
    myDrawLine(rho, theta, imgHough, (0, 0, 255), 1)
# myShow(fileName+'_Hough', imgHough)
