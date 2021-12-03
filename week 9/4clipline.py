import numpy as np
import cv2 as cv

retval, pt1, pt2 = cv.clipLine((100, 100, 455, 455),(0, 10), (455, 455))
print(retval, pt1, pt2)

img1 = np.zeros((512, 512, 3), np.uint8)

cv.line(img1, (0, 10), (455, 455), (64, 0, 64), 3, cv.FILLED, 0)
cv.rectangle(img1, (100, 100), (455, 455), (0, 255, 0), 0)
cv.imshow("Display window", img1)

key = cv.waitKey(0)
if key == ord("s"):
    cv.imwrite("makeImage.jpg", img1)
