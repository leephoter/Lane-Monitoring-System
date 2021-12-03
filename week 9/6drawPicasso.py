import numpy as np
import cv2 as cv
import math

sx, sy, ex, ey = -1, -1, -1, -1

def myDrawing(event, x, y, flags, param):
    global sx, sy, ex, ey
    if event == cv.EVENT_LBUTTONDOWN:
        sx, sy = x, y
    elif event == cv.EVENT_LBUTTONUP:
        ex, ey = x, y
        cv.rectangle(img, (sx, sy), (ex, ey), (0, 128, 64), 2)
    if event == cv.EVENT_RBUTTONDOWN:
        sx, sy = x, y
    elif event == cv.EVENT_RBUTTONUP:
        ex, ey = x, y
        r = int(math.sqrt((sx-ex)*(sx-ex)+(sy-ey)*(sy-ey)))
        cv.circle(img, (sx, sy), r, (64, 0, 64), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('Picasso')
cv.setMouseCallback('Picasso', myDrawing)

while(1):
    cv.imshow('Picasso', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
