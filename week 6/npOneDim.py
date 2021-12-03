import numpy as np

a1 = np.arange(0,24,2)
print("1",a1)

for i in range(a1.size):
    a1[i] *= 3
print("3",a1)

print("4", a1[1:5])

print("5",a1[np.arange(5)])

b1 = np.array([False, True, False, True, False, True, False, True, False, True, False, True])
print("6", a1[b1])
