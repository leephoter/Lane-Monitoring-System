import numpy as np
import cv2 as cv
from random import *

def findPosition(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        img[y][x] = [0,0,255]
        font = cv.FONT_HERSHEY_COMPLEX
        text = "("+ str(x) + ", "+ str(y) + ")"
        cv.putText(img, text, (x+5, y+5), font, 0.4, (128, 0, 255), 1, cv.LINE_AA)

img = cv.imread(cv.samples.findFile("car.jpg"))
if img is None:
    sys.exit("Could not read the image.")

cv.namedWindow('car')
cv.setMouseCallback('car', findPosition)

while(1):
    cv.imshow('car', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()