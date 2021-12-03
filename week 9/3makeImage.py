import numpy as np
import cv2 as cv

print("OpenCV version :  ",cv.__version__)

img1 = np.zeros((512, 512, 3), np.uint8)
for r in range(256):
    for c in range(256):
        img1[r, c, 0] = 100
        img1[r, c, 1] = 100
        img1[r, c, 2] = 100

for r in range(256):
    for c in range(256, 512):
        img1[r, c, 0] = r
        img1[r, c, 1] = r
        img1[r, c, 2] = r

cv.imshow("img1", img1)

cv.line(img1, (511, 0), (0, 511), (64, 0, 64), 3, cv.FILLED, 0)
cv.rectangle(img1, (100, 100), (455, 455), (0, 255, 0), 0)
point1 = np.array([[50,50], [260, 90], [10, 300]], np.int32)
point2 = np.array([[250,250], [460, 490], [410, 130], [300, 500]], np.int32)
cv.fillConvexPoly(img1, point1, (120, 14, 25))
cv.fillPoly(img1, [point1, point2], (100, 44, 55))
cv.circle(img1, (255, 255), 128, (0, 128, 128), 2)
cv.ellipse(img1, (255,255), (200,50), 0.0, 45.0, 275.0, (128, 64, 255))
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img1, 'my future', (10, 256), font, 2, (128, 0, 255), 2, cv.LINE_AA)
cv.imshow("Display window", img1)

retval, pt1, pt2 = cv.clipLine((100, 100, 455, 455),(10, 10), (455, 455))
print(retval, pt1, pt2)
key = cv.waitKey(0)
if key == ord("s"):
    cv.imwrite("makeImage.jpg", img1)
