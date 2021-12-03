'''
Gray -> ROI -> Threshold-> Canny -> HoughLine -> Angle of Lines -> Average Lines
-> Detecting & displaying the lane -> Topview of the lane

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
syROI = 232
eyROI = 369
pointRoi = np.array([[270, 220], [205, 350], [470, 350], [330, 220]], np.int32)
cv.fillConvexPoly(imgRoi, pointRoi, 255)
imgRoiDisp = cv.addWeighted(imgGray, 0.8, imgRoi, 0.2, 0)
myShow('Original', img)
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
edges = cv.Canny(thresh, 50, 150)
# myShow(fileName+'_Canny', edges)

# Hough Line
lines = cv.HoughLines(edges, 1, np.pi/200, 21)  # 30, 20

imgHough = np.copy(img)

thetaQ = np.array([0.0, 0.0])
rhoQ = np.array([0.0, 0.0])
countQ = np.array([0.0, 0.0])

pt1 = np.array([[0, 0], [0, 0]])
pt2 = np.array([[0, 0], [0, 0]])

for line in lines:
    rho, theta = line[0]
# Angle of Lines
    if(theta < np.pi*27/180 and theta > np.pi*26/180):
        thetaQ[0] = thetaQ[0] + theta
        rhoQ[0] = rhoQ[0] + rho
        countQ[0] = countQ[0] + 1
    if(theta < np.pi*130/180 and theta > np.pi*129/180):
        thetaQ[1] = thetaQ[1] + theta
        rhoQ[1] = rhoQ[1] + rho
        countQ[1] = countQ[1] + 1
# myShow(fileName+'_Hough1', imgHough)
# Average lines
for i in range(2):
    thetaQ[i] = thetaQ[i] / countQ[i]
    rhoQ[i] = rhoQ[i] / countQ[i]
    p1, p2 = myDrawLine(rhoQ[i], thetaQ[i], imgHough, (0, 0, 255), 1)

# Detecting the lane
    retval, pt1[i], pt2[i] = cv.clipLine((0, syROI, 511, eyROI-syROI), tuple(p1), tuple(p2))
    cv.rectangle(imgHough, (0, syROI), (600, eyROI), (0, 238, 255), 3)
    print(retval, pt1[i], pt2[i])
cv.rectangle(imgHough, tuple(pt1[0]), tuple(pt2[0]), (179, 255, 0), 3)
cv.rectangle(imgHough, tuple(pt1[1]), tuple(pt2[1]), (255, 0, 162), 3)
# myShow(fileName+'_Hough2', imgHough)

# Displaying the lane
point = np.array([pt2[0],  pt1[0], pt2[1], pt1[1]], np.int32)
cv.fillConvexPoly(imgOut, point, (255, 0, 0))
overlapImage = cv.addWeighted(img, 0.6, imgOut, 0.4, 0)
# myShow(fileName+'_Lane', overlapImage)

# Topview of the lane
pts2 = np.float32([[0, 0], [0, 512], [512, 512], [512, 0]])
pts1 = np.float32([pt2[0],  pt1[0], pt2[1], pt1[1]])

M = cv.getPerspectiveTransform(pts1, pts2)
perspectiveImg = cv.warpPerspective(img, M, (512, 512))
# myShow(fileName+'_TopView', perspectiveImg)
