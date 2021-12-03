'''
Gray ->  Canny -> ROI -> HoughLine -> Angle of Lines -> Average Lines
-> Detecting & displaying the lane -> Topview of the lane

'''
import cv2 as cv
import numpy as np
from doImage import *
from math import *

fileName = 'express'

img = cv.imread(fileName+'.jpg')

# Gray
imgGray = cv.imread(fileName+'.jpg', 0)
imgRoi = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
imgOut = np.zeros(img.shape, np.uint8)

# Region Of Interest
syROI = 209
eyROI = 317
pointRoi = np.array([[261, 209], [0, 317], [510, 317],
                    [340, 209]], np.int32)  # ROI
cv.fillConvexPoly(imgRoi, pointRoi, 255)
imgRoiDisp = cv.addWeighted(imgGray, 0.8, imgRoi, 0.2, 0)
myShow(fileName+'_Roi', imgRoiDisp)

# Canny
edges = cv.Canny(imgGray, 250, 300)
myShow(fileName+'_Canny', edges)

# Region Of Interest
for r in range(0, img.shape[0]):
    for c in range(0, img.shape[1]):
        if(imgRoi[r, c] == 0):
            edges[r, c] = 0
myShow(fileName+'_roiEdge', edges)

# Hough Line
lines = cv.HoughLines(edges, 1, np.pi/180, 20)  # 30, 20

imgHough = np.copy(img)

thetaQ = np.array([0.0, 0.0])
rhoQ = np.array([0.0, 0.0])
countQ = np.array([0.0, 0.0])

pt1 = np.array([[0, 0], [0, 0]])
pt2 = np.array([[0, 0], [0, 0]])

for line in lines:
    rho, theta = line[0]
# Angle of Lines
    if(theta < np.pi*60/180 and theta > np.pi*50/180):
        thetaQ[0] = thetaQ[0] + theta
        rhoQ[0] = rhoQ[0] + rho
        countQ[0] = countQ[0] + 1
    if(theta < np.pi*130/180 and theta > np.pi*120/180):
        thetaQ[1] = thetaQ[1] + theta
        rhoQ[1] = rhoQ[1] + rho
        countQ[1] = countQ[1] + 1
myShow(fileName+'_Hough', imgHough)
# Average lines
for i in range(2):
    thetaQ[i] = thetaQ[i] / countQ[i]
    rhoQ[i] = rhoQ[i] / countQ[i]
    p1, p2 = myDrawLine(rhoQ[i], thetaQ[i], imgHough, (0, 0, 255), 1)

# Detecting the lane
    retval, pt1[i], pt2[i] = cv.clipLine((0, syROI, 511, eyROI-syROI), p1, p2)
    cv.rectangle(imgHough, [0, syROI], [511, eyROI], (0, 128, 0), 2)
    print(retval, pt1[i], pt2[i])
cv.rectangle(imgHough, pt1[0], pt2[0], (0, 128, 256), 2)
cv.rectangle(imgHough, pt1[1], pt2[1], (128, 0, 0), 2)
myShow(fileName+'_Hough', imgHough)

# Displaying the lane
point = np.array([pt2[0],  pt1[0], pt2[1], pt1[1]], np.int32)
cv.fillConvexPoly(imgOut, point, (255, 0, 0))
overlapImage = cv.addWeighted(img, 0.6, imgOut, 0.4, 0)
myShow(fileName+'_Lane', overlapImage)

# Topview of the lane
pts2 = np.float32([[0, 0], [0, 512], [512, 512], [512, 0]])
pts1 = np.float32([pt2[0],  pt1[0], pt2[1], pt1[1]])

M = cv.getPerspectiveTransform(pts1, pts2)
perspectiveImg = cv.warpPerspective(img, M, (512, 512))
myShow(fileName+'_TopView', perspectiveImg)
