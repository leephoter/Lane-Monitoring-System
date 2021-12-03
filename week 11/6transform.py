import numpy as np
import cv2 as cv
import time

def myShow( title,  img):
    cv.imshow(title, img)
    if cv.waitKey(0) & 0xFF == 27:
        cv.destroyAllWindows()
        exit(0)
    else:
        cv.destroyWindow(title)

img = cv.imread('256_love.jpg')
cv.imshow('original', img)
rows, cols, ch = img.shape

M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 45, 1)
rotationImg = cv.warpAffine(img, M, (cols, rows))
myShow('rotation', rotationImg)

pts1 = np.float32([[0, 0], [255, 0], [0, 255]])
pts2 = np.float32([[100, 100], [200, 64], [0, 255]])
M = cv.getAffineTransform(pts1, pts2)
affineImg = cv.warpAffine(img, M, (cols, rows))
myShow('affine', affineImg)

pts1 = np.float32([[0, 0], [255, 0], [0, 255], [255, 255]])
pts2 = np.float32([[55, 128], [200, 128], [0, 255], [255, 255]])
M = cv.getPerspectiveTransform(pts1, pts2)
perspectiveImg = cv.warpPerspective(img, M, (300, 300))
cv.rectangle(perspectiveImg, (0, 0), (254, 254), (0, 128, 64), 2)
myShow('perspective', perspectiveImg)

cv.destroyAllWindows()