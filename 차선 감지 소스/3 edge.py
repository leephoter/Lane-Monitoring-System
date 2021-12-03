import numpy as np
import cv2 as cv
from doImage import *

img = cv.imread('straight22.jpg', 0)
myShow('straight22', img)

laplacian = cv.Laplacian(img, cv.CV_8U)
myShow('laplacian', laplacian)
sobelx = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=3)
myShow('sobelx', sobelx)
sobely = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=3)
myShow('sobely', sobely)
