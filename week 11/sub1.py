#  -*- coding: utf-8 -*-
import numpy as np 
import cv2 as cv

img_org = cv.imread("image1.jpg")
img = np.copy(img_org)

x_down, y_down, x_up, y_up = np.zeros(4, dtype=np.uint8)
def Click(event, x, y, flags, param):
    global x_down, y_down, x_up, y_up
    if event == 2:
        if x_down > x_up:
            x_down, x_up = x_up, x_down
        if y_down > y_up:
            y_down, y_up = y_up, y_down

        img_event = np.copy(img_org[y_down:y_up+1, x_down:x_up+1])

        x_len, y_len = x_up - x_down + 1, y_up - y_down + 1 
        x_hlen, y_hlen = x_len // 2, y_len // 2
        y_left = y - y_hlen
        y_right = y + y_hlen + y_len % 2
        x_left = x - x_hlen
        x_right = x + x_hlen + x_len % 2
        y_ld, y_rd, x_ld, x_rd = np.zeros(4, dtype=np.int8)
        if y_left < 0:
            y_ld = -y_left
            y_left = 0 
        if x_left < 0:
            x_ld = -x_left
            x_left = 0
        if x_right > 255:
            x_rd = x_right - 255
            x_right = 255 
        if y_right > 255:
            y_rd = y_right - 255
            y_right = 255
        img[y_left : y_right , x_left : x_right] = img_event[y_ld:y_len-y_rd,x_ld:x_len-x_rd]
        cv.imshow("img", img)

    if event == 1:
        x_down, y_down = x, y 
        img_org[:,:] = img[:,:] 
        cv.setMouseCallback("img", Drag)

def Mouse_up(x, y):
    global x_up, y_up
    x_up = x
    y_up = y
    cv.imshow('img', img_org) 
    cv.setMouseCallback("img", Click)

def Drag(event, x, y, flags, param):
    global x_down, y_down
    xx = x_down
    yy = y_down

    if event == 0:
        img = np.copy(img_org)
        cv.rectangle(img, (xx, yy), (x, y), (0, 255, 255)) 
        cv.imshow('img', img)

    if event == 4:
        Mouse_up(x, y)

def Mouse_down(event, x, y, flags, param):
    global x_down, y_down 
    if event == 1:
        x_down, y_down = x, y
        cv.setMouseCallback("img", Drag)

cv.namedWindow("img") 
cv.setMouseCallback("img", Mouse_down) 
cv.imshow("img",img_org)
cv.waitKey(0)
  
cv.destroyAllWindows()