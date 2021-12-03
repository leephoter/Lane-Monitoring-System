import cv2 as cv
import numpy as np


def thresholding1(x):
    global thresh1, img_thresh1
    global hist1, img1
    ret, thresh1 = cv.threshold(hist1, x, 255, cv.THRESH_BINARY)
    ret, img_thresh1 = cv.threshold(img1, x, 255, cv.THRESH_BINARY)


def thresholding2(x):
    global thresh2, img_thresh2
    global hist2, img2
    ret, thresh2 = cv.threshold(hist2, x, 255, cv.THRESH_BINARY)
    ret, img_thresh2 = cv.threshold(img2, x, 255, cv.THRESH_BINARY)


def thresholding3(x):
    global thresh3, img_thresh3
    global hist3, img3
    ret, thresh3 = cv.threshold(hist3, x, 255, cv.THRESH_BINARY)
    ret, img_thresh3 = cv.threshold(img3, x, 255, cv.THRESH_BINARY)


img1 = cv.imread('free22.jpg', 0)
img2 = cv.imread('straight22.jpg', 0)
img3 = cv.imread('curved22.jpg', 0)

hist1 = cv.equalizeHist(img1)
hist2 = cv.equalizeHist(img2)
hist3 = cv.equalizeHist(img3)

cv.namedWindow('threshold')
cv.createTrackbar('free22', 'threshold', 0, 255, thresholding1)
cv.createTrackbar('straight22', 'threshold', 0, 255, thresholding2)
cv.createTrackbar('curved22', 'threshold', 0, 255, thresholding3)

ret, thresh1 = cv.threshold(hist1, 0, 255, cv.THRESH_BINARY)
ret, img_thresh1 = cv.threshold(img1, 0, 255, cv.THRESH_BINARY)

ret, thresh2 = cv.threshold(hist2, 0, 255, cv.THRESH_BINARY)
ret, img_thresh2 = cv.threshold(img2, 0, 255, cv.THRESH_BINARY)

ret, thresh3 = cv.threshold(hist3, 0, 255, cv.THRESH_BINARY)
ret, img_thresh3 = cv.threshold(img3, 0, 255, cv.THRESH_BINARY)

cv.imshow('free22Hist', thresh1)
cv.imshow('straightHist', thresh2)
cv.imshow('curvedHist', thresh3)

cv.imshow('free22', img_thresh1)
cv.imshow('straight22', img_thresh2)
cv.imshow('curved22', img_thresh3)

while(1):
    cv.imshow('free22Hist', thresh1)
    cv.imshow('straightHist', thresh2)
    cv.imshow('curvedHist', thresh3)
    cv.imshow('free22', img_thresh1)
    cv.imshow('straight22', img_thresh2)
    cv.imshow('curved22', img_thresh3)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('s') or k == ord('S'):
        cv.imwrite('Thresh_free22Hist.jpg', thresh1)
        cv.imwrite('Thresh_straightHist.jpg', thresh2)
        cv.imwrite('Thresh_curvedHist.jpg', thresh3)
        cv.imwrite('Thresh_free22.jpg', img_thresh1)
        cv.imwrite('Thresh_straight.jpg', img_thresh2)
        cv.imwrite('Thresh_curved.jpg', img_thresh3)
        break

cv.destroyAllWindows()
