#  -*- coding: utf-8 -*-

import numpy as np 
import cv2 as cv
sample1 = cv.resize(cv.imread("image1.jpg"),(256,256)) 
image1 = cv.resize(cv.imread("image2.jpg"),(256,256)) 
image2 = cv.resize(cv.imread("image4.jpg"),(256,256))
cv.imshow('sample1', sample1) 
cv.imshow('image1', image1) 
cv.imshow('image2', image2)
np.random.seed(seed=5) 
for i in range(9):
    img = np.zeros((256, 256, 3), dtype=np.int8) 
    rimg = [0, 1, 2]
    np.random.shuffle(rimg)
    rn = np.random.randint(low=0, high=2, size=3) 
    img[:,:,rimg[0]] = sample1[:,:,rn[0]] 
    img[:,:,rimg[1]] = image1[:,:,rn[1]] 
    img[:,:,rimg[2]] = image2[:,:,rn[2]]
    cv.imshow('img{0}'.format(i+1), img)
cv.waitKey(0) 
cv.destroyAllWindows()