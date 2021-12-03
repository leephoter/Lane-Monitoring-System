#  -*- coding: utf-8 -*- 
import cv2 as cv;
import sys
import numpy as np;
import time

img = cv.imread("512faces.jpg")
grayImg = cv.imread('512faces.jpg', 0)

print(img.shape)

rowSize, colSize, channels = img.shape

print("rowSize:%d colSize:%d channels:%d" % (rowSize, colSize, channels))
print("img.size : %d" % (img.size))
print(img.dtype)

# # img[:, :, 0] = 1
# img[:, :, 1] = 1
# # img[:, :, 2] = 1
# ------------직접 설정


cv.imshow("result1", img)
for r in range(rowSize):
    for c in range(colSize):
        if(img[r,c,0] >= 10 and img[r,c,0] <= 255 or img[r,c,0] >= 80 and 
        img[r,c,0] <= 200 or img[r,c,0] >= 9 and img[r,c,0] <= 15):
            img[r, c] = [10, 20, 150] # img[r,c] == img[r,c,:]
#----------------해당 픽셀 찾아서 바꾸기


cv.imshow("result2", img)

cv.waitKey(0)
cv.destroyAllWindows()