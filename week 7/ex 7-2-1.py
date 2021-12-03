import numpy as np
SIZE = 30

a = np.arange(1, SIZE+1)
print(a)
sum = 0
for i in range(0, SIZE, 2):
    sum += a[i]
print("sum = %d"%(sum))
