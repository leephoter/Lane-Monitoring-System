import numpy as np

a1 = np.arange(0,24,2)
# print("1",a1)

for i in range(a1.size): #0~11
    a1[i] *= 3 # a1[2] = a1[2] * 3
print("3",a1)

# print("4", a1[1:5])
# print("5",a1[np.arange(1,5)])

b1 = np.array(
    [False, True, False, True, False, True, False, True, False, True, False, True]
)   #0      6       32                                                        66          
print(b1)
print("6", a1[b1])
# a1[False]   #0
# a1[True]    #6
# ...
