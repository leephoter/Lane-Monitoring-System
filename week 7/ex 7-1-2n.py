import numpy as np

def dispArray(a, r, c):
    for i in range(r):
        print(" | ", end="")
        for j in range(c):
            print("%3d " % a[i, j], end="")
        print("|")

a1 = np.arange(1, 25)
i = 0
for r in range(2, 24):
    if 24 % r == 0:
        i += 1
        c = 24//r
        print("(%d) %d x %d ====================" % (i, r, c))
        a2 = a1.reshape(r, c, 1)
        dispArray(a2, r, c)
