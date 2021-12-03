import numpy as np
import cv2 as cv
from random import *

img1 = np.zeros((512, 512, 3), np.uint8)

size = 16
i = 0
for r in range(0, 512, size):
    color = i % 2
    i += 1
    for c in range(0, 512, size):
        if color==0:
            cv.rectangle(img1, (c, r), (c+size-1, r+size-1), (212, 215, 73), -1)
            color = 1
        else:
            cv.rectangle(img1, (c, r), (c+size-1, r+size-1), (182, 133, 39), -1)
            color = 0

cv.imshow("pattern", img1)

key = cv.waitKey(0)

