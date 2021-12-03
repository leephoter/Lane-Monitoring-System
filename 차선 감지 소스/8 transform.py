import numpy as np
import cv2 as cv
import time
from doImage import *

img = cv.imread('straight22.jpg')
cv.imshow('original', img)
rows, cols, ch = img.shape

pts1 = np.float32([[0, 0], [0, 512], [512, 512], [512, 0]])
pts2 = np.float32([[128, 256], [0, 511], [511, 511], [384, 256]])
M = cv.getPerspectiveTransform(pts1, pts2)
perspectiveImg = cv.warpPerspective(img, M, (512, 512))
#cv.rectangle(perspectiveImg, (0, 0), (254, 254), (0, 128, 64), 2)
myShow('perspective', perspectiveImg)
