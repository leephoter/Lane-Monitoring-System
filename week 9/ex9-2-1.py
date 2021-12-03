import numpy as np
import cv2 as cv
from random import *
'''
cv.EVENT_MOUSEMOVE
cv.EVENT_LBUTTONDOWN
cv.EVENT_RBUTTONDOWN
cv.EVENT_MBUTTONDOWN
cv.EVENT_LBUTTONUP
cv.EVENT_RBUTTONUP
cv.EVENT_MBUTTONUP
cv.EVENT_LBUTTONDBLCLK
cv.EVENT_RBUTTONDBLCLK
cv.EVENT_MBUTTONDBLCLK
cv.EVENT_MOUSEWHEEL
cv.EVENT_MOUSEHWHEEL
'''
def drawCircle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        cv.circle(img, (x, y), randint(2,30), color, -1)

img = cv.imread(cv.samples.findFile("512faces.jpg"))
if img is None:
    sys.exit("Could not read the image.")

cv.namedWindow('512faces')
cv.setMouseCallback('512faces', drawCircle)

while(1):
    cv.imshow('512faces', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
