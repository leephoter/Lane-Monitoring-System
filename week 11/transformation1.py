import numpy as np
import cv2 as cv
import time

def myShow(title,  img):
    cv.imshow(title, img)
    if cv.waitKey(0) & 0xFF == 27:
        cv.destroyAllWindows()
        exit(0)
    else:
        cv.destroyWindow(title)

img = cv.imread('256_love.jpg')
cv.imshow('original', img)
rows, cols, ch = img.shape

resizeImg1 = cv.resize(img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
myShow('resize1.5', resizeImg1)

resizeImg2 = cv.resize(img, (2*cols, 2*rows), interpolation=cv.INTER_CUBIC)
myShow('resize2', resizeImg2)

M = np.float32([[0, 1, 100], [1, 0, 10]])
warpImg = cv.warpAffine(img, M, (cols, rows))
myShow('warp', warpImg)

cv.destroyAllWindows()
