import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt


def myShow(title,  img):
    cv.imshow(title, img)
    key = cv.waitKey(0)
    if key & 0xFF == 27:
        cv.destroyAllWindows()
        exit(0)
    elif key == ord('d') or key == ord('D'):
        cv.destroyWindow(title)
    elif key == ord('s') or key == ord('S'):
        cv.imgwrite(title+".jpg", img)
        cv.destroyWindow(title)
    else:
        pass


def myPltShow(title,  img):
    plt.imshow(img)
    plt.title(title)
    plt.show()


def myDrawLine(rho, theta, img, color, thick):
    x0 = rho * np.cos(theta)
    y0 = rho * np.sin(theta)
    x1 = int(x0 - 1000*np.sin(theta))
    y1 = int(y0 + 1000*np.cos(theta))
    x2 = int(x0 + 1000*np.sin(theta))
    y2 = int(y0 - 1000*np.cos(theta))
    cv.line(img, (x1, y1), (x2, y2), color, thick)
    return [x1, y1], [x2, y2]
