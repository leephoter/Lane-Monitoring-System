import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('straight22.jpg')

kernel_5 = np.ones((5, 5), np.float32)/25
filteredImg5 = cv.filter2D(img, -1, kernel_5)
cv.imshow("filteredImg5", filteredImg5)
kernel_11 = np.ones((11, 11), np.float32)/121
filteredImg11 = cv.filter2D(img, -1, kernel_11)
cv.imshow("filteredImg11", filteredImg11)
key = cv.waitKey(0)
cv.destroyAllWindows()

blurImg5 = cv.blur(img, (5, 5))
cv.imshow("blurImg5", blurImg5)
blurImg11 = cv.blur(img, (11, 11))
cv.imshow("blurImg11", blurImg11)
key = cv.waitKey(0)
cv.destroyAllWindows()

GaussianImg5 = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("GaussianImg5", GaussianImg5)
GaussianImg11 = cv.GaussianBlur(img, (11, 11), 0)
cv.imshow("GaussianImg11", GaussianImg11)
GaussianImg5_7 = cv.GaussianBlur(img, (5, 5), 0.7)
cv.imshow("GaussianImg5_7", GaussianImg5_7)
key = cv.waitKey(0)
cv.destroyAllWindows()

medianImg5 = cv.medianBlur(img, 5)
cv.imshow("medianImg5", medianImg5)
medianImg11 = cv.medianBlur(img, 11)
cv.imshow("medianImg11", medianImg11)
key = cv.waitKey(0)
cv.destroyAllWindows()

bilatImg5_75 = cv.bilateralFilter(img, 5, 75, 75)
cv.imshow("bilatImg5_75", bilatImg5_75)
bilatImg11_75 = cv.bilateralFilter(img, 11, 75, 75)
cv.imshow("bilatImg11_75", bilatImg11_75)
bilatImg11_200 = cv.bilateralFilter(img, 11, 200, 200)
cv.imshow("bilatImg11_200", bilatImg11_200)
key = cv.waitKey(0)
cv.destroyAllWindows()

titles = ['original', "filteredImg", 'blur',
          'GaussianBlur', 'medianBlur', 'bilateralFilter']
images = [img, filteredImg5, blurImg5, GaussianImg5, medianImg5, bilatImg5_75]

plt.rc('font', size=8)
plt.rc('axes', titlesize=12)
for i in range(6):
    fig, ax = plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
