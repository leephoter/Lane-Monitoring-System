import numpy as np

a1 = np.arange(1, 25)
i = 0
# print(a1)
for r in range(2,24):
    if 24%r==0:
        i += 1
        c = 24//r
        print("(%d) %d x %d ===================="%(i,r,c))
        a2 = a1.reshape(r, c)
        print(a2)