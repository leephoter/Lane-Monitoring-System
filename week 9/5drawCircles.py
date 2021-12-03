import numpy as np
import cv2 as cv
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
def drawFlower(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 5, (39, 127, 255), 1)

img = cv.imread(cv.samples.findFile("512flower.jpg"))
if img is None:
    sys.exit("Could not read the image.")

cv.namedWindow('512flower')
cv.setMouseCallback('512flower', drawFlower)

while(1):
    cv.imshow('512flower', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
