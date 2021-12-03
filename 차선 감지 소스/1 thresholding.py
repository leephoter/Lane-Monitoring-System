import cv2 as cv
import numpy as np


def thresholding1(x):
    global thresh1
    global img1
    ret, thresh1 = cv.threshold(img1, x, 255, cv.THRESH_BINARY)


def thresholding2(x):
    global thresh2
    global img2
    ret, thresh2 = cv.threshold(img2, x, 255, cv.THRESH_BINARY)


def thresholding3(x):
    global thresh3
    global img3
    ret, thresh3 = cv.threshold(img3, x, 255, cv.THRESH_BINARY)


img1 = cv.imread('free22.jpg', 0)
img2 = cv.imread('straight22.jpg', 0)
img3 = cv.imread('curved22.jpg', 0)

cv.namedWindow('exp_thresh')
cv.createTrackbar('T', 'exp_thresh', 0, 255, thresholding1)
cv.namedWindow('str_thresh')
cv.createTrackbar('T', 'exp_thresh', 0, 255, thresholding2)
cv.namedWindow('cur_thresh')
cv.createTrackbar('T', 'exp_thresh', 0, 255, thresholding3)

cv.imshow('free22', img1)
ret, thresh1 = cv.threshold(img1, 0, 255, cv.THRESH_BINARY)
cv.imshow('straight2', img2)
ret, thresh2 = cv.threshold(img2, 0, 255, cv.THRESH_BINARY)
cv.imshow('curved2-1', img3)
ret, thresh3 = cv.threshold(img3, 0, 255, cv.THRESH_BINARY)

while(1):
    cv.imshow('exp_thresh', thresh1)
    cv.imshow('str_thresh', thresh2)
    cv.imshow('cur_thresh', thresh3)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
