import numpy as np
import cv2 as cv
from random import *

img1 = np.zeros((512, 512, 3), np.uint8)

for no in range(5):
    size = 100
    for i in range(1000):
        sr = randint(0, 511-size)
        sc = randint(0, 511-size)
        er = sr + randint(5, size)
        ec = sc + randint(5, size)
        cv.rectangle(img1, (sc, sr), (ec, er), (randint(0, 255),randint(0, 255), randint(0, 255)), -1)
        er = randint(0+size, 511)
        ec = randint(0+size, 511)
        sr = er - randint(5, size)
        sc = ec - randint(5, size)
        cv.rectangle(img1, (sc, sr), (ec, er), (randint(0, 255), randint(0, 255), randint(0, 255)), -1)

    cv.imshow("colorSquares {}".format(no), img1)

key = cv.waitKey(0)

