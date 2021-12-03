#  -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import time 
isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue, red = (255, 0, 0), (0, 0, 255)
turn = 0
img = cv.imread('image2.jpg')
def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img, turn, roi, w, h
    if event == cv.EVENT_LBUTTONDOWN:
        isDragging = True
        x0, y0 = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv.rectangle(img_draw, (x0,y0),(x,y),blue,2)
            cv.imshow('img', img_draw)
    elif event == cv.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x-x0
            h = y-y0
            if w>0 and h>0:
                img_draw = img.copy()
                cv.rectangle(img_draw, (x0,y0),(x, y), red, 2)
                cv.imshow('img', img_draw)
                roi = img[y0:y0+h, x0:x0+w]
                cv.imwrite("new img.jpg", roi)
                cv.imshow("new img",roi)
            else:
                cv.imshow('img',img)
                print('왼쪽부터 드래그를 하세요')
cv.imshow('img',img)
cv.setMouseCallback('img', onMouse)
cv.waitKey()
cv.destroyAllWindows()