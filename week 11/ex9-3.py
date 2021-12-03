import cv2 as cv
import numpy as np
import sys
import random


def checkColor(pix):
    # print(pix)
    if(pix[0] == 0 and pix[1] == 0 and pix[2] == 0):
        return 1
    elif(pix[0] == 255 and pix[1] == 255 and pix[2] == 255):
        return 0
    return 2


def putColor(r, c, color):
    global rsize
    global csize
    global que
    global qno
    for n in range(-1, 2, 2):
        if(r+n >= 0 and r+n < rsize and checkColor(img[r+n, c]) == 0):
            img[r+n, c] = color
            que[qno, 0] = r+n
            que[qno, 1] = c
            qno = qno + 1
            # print(qno)
        if(c+n >= 0 and c+n < csize and checkColor(img[r, c+n]) == 0):
            img[r, c+n] = color
            que[qno, 0] = r
            que[qno, 1] = c+n
            qno = qno + 1
            # print(qno)


img = cv.imread("circles.jpg")
if img is None:
    sys.exit("Could not read the image.")

rsize, csize, channel = img.shape
print("rsize:%d, csize:%d" % (rsize, csize))
for r in range(rsize):
    for c in range(csize):
        if(img[r, c, 0] < 10 and img[r, c, 1] < 10 and img[r, c, 2] < 10):
            img[r, c] = [0, 0, 0]
        else:
            img[r, c] = [255, 255, 255]
cv.imwrite("hahaha.jpg", img)
que = np.zeros((65536, 2), dtype=np.int16)
qno = 0

for r in range(rsize):
    for c in range(csize):
        if(checkColor(img[r, c]) == 0):
            rClr = random.randint(0, 255)
            gClr = random.randint(0, 255)
            bClr = random.randint(0, 255)
            color = [bClr, gClr, rClr]
            img[r, c] = color
            putColor(r, c, color)
            while(qno > 0):
                qno = qno - 1
                r1 = que[qno, 0]
                c1 = que[qno, 1]
                putColor(r1, c1, color)


cv.imshow("HOHOHO", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("colored.jpg", img)
