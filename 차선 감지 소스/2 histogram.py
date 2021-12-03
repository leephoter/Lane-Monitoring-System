import cv2 as cv

img = cv.imread('free22.jpg')
if img is None:
    print('Could not open or find the image:')
    exit(0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayEq = cv.equalizeHist(gray)
cv.imshow('original', gray)
cv.imshow('equalized', grayEq)
cv.waitKey()
