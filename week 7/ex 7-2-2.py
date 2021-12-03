import numpy as np

a = np.arange(1, 31)
print(a)
sumE = 0
sumO = 0
for i in range(0, 30, 2):
    sumE += a[i]
    sumO += a[i+1]
diff = abs(sumE-sumO)
print("diff=%d sumE=%d sumO=%d"%(diff, sumE, sumO))
