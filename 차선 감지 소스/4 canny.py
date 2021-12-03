import numpy as np
import cv2 as cv
from doImage import *

img = cv.imread('straight22.jpg', 0)
myShow('straight22', img)

canny1 = cv.Canny(img, 0, 50)
canny2 = cv.Canny(img, 0, 200)
canny3 = cv.Canny(img, 100, 200)
myShow('canny1', canny1)
myShow('canny2', canny2)
myShow('canny3', canny3)
