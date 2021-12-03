import numpy as np

a = np.arange(1, 31)
print(a)
b = np.arange(0, 15)

for i in range(0, 15):
    b[i] = a[i] * a[29-i]
print(b)

