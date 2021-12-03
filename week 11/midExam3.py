import numpy as np

for n in range(2, 14, 3):
    print(n)

A = np.zeros((6, 10))
print(A)

A[1:5, 1:9] = 100
print(A)
