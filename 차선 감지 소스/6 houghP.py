import cv2 as cv
import numpy as np
from doImage import *
import copy

img = cv.imread(cv.samples.findFile('straight22.jpg'))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150)

lines = cv.HoughLinesP(edges, 1, np.pi/20, 200,
                       minLineLength=100, maxLineGap=100)

imgHough = copy.copy(img)
for line in lines:
    print(line)
    x1, y1, x2, y2 = line[0]
    
    cv.line(imgHough, (x1, y1), (x2, y2), (0, 0, 255), 2)
myShow('houghlines', imgHough)
