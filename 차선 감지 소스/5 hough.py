import cv2 as cv
import numpy as np
from doImage import myShow


def drawLine(rho, theta, img, color, thick):
    x0 = rho * np.cos(theta)
    y0 = rho * np.sin(theta)
    x1 = int(x0 - 1000*np.sin(theta))
    y1 = int(y0 + 1000*np.cos(theta))
    x2 = int(x0 + 1000*np.sin(theta))
    y2 = int(y0 - 1000*np.cos(theta))
    cv.line(img, (x1, y1), (x2, y2), color, thick)
    return [x1, y1], [x2, y2]


img = cv.imread(cv.samples.findFile('straight22.jpg'))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150)
cv.imshow('Edges', edges)

lines = cv.HoughLines(edges, 1, np.pi/2, 150)
imgHough = np.copy(img)

for line in lines:
    rho, theta = line[0]
    drawLine(rho, theta, imgHough, (0, 0, 255), 1)
myShow('houghlines', imgHough)
