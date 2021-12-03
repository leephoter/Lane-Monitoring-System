import numpy as np
import math
SIZE = 7

a = np.arange(1, SIZE*SIZE+1).reshape(SIZE, SIZE)
b = np.arange(1, SIZE*SIZE+1).reshape(SIZE, SIZE)

for r in range(SIZE):
    for c in range(SIZE):
        a[r, c] = r+1 + c*SIZE
print(a)

print("-------------------------------------------------")
for r in range(0, SIZE):
    for c in range(0, SIZE):
        if( (r>1 and r<5) and (c>1 and c<5) ):
            b[r, c] = a[r, c]
        else:
            if(r <= 1 or c <= 1 or c >= 5 or  r >= 5):
                c1 = 6-r
                r1 = c
                b[r1, c1] = a[r, c]
print(b)
