#  -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import time 
def myShow(title, img):
    cv.imshow(title, img)
    if cv.waitKey(0) & 0XFF == 27:
        cv.destroyAllwindows()
        exit(0)
    else:
        cv.destroyWindow(title)
img = cv.imread('image1.jpg')
cv.imshow("meet",img)
row, cols, ch = img.shape
M = cv.getRotationMatrix2D(((cols-1)/2.0, (row-1)/2.0), 45, 1)
rotationImg = cv.warpAffine(img, M, (cols, row))
myShow("rotation", rotationImg)
pts1 = np.float32([[0,0], [0,255], [255,0]])
pts2 = np.float32([[100,100], [0,255],[255,0]])
M = cv.getAffineTransform(pts1, pts2)
affineImg = cv.warpAffine(img, M, (cols, row))
myShow("affine", affineImg)
pts1 = np.float32([[0,0], [0,255], [255,0], [255,255]])
pts2 = np.float32([[0,0], [0,255], [255,0], [255,255]])
M = cv.getPerspectiveTransform(pts1, pts2)
perspctiveImg = cv.warpPerspective(img, M, (500,500))
cv.rectangle(perspctiveImg, (0,0), (254,254), (0,128,64), 2)
myShow("perspective", perspctiveImg)
cv.destroyAllWindows()