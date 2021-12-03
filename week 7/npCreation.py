import numpy as np

a1 = np.arange(1,13)
# print("1", a1)
# print("2", a1.shape) #길이??
# print("3", a1.ndim)     #몇차원인가
# print("4", a1.dtype.name)   #
# print("5", a1.itemsize) #몇바이트냐
# print("6", a1.size) #길이
# print("7",  type(a1) )

a2 = a1.reshape(2, 3, 2)
# print("11", a2)
# print("12", a2.shape)
# print("13", a2.ndim)
# print("14", a2.dtype.name)
# print("15", a2.itemsize)
# print("16", a2.size)
# print("17",  type(a2))

a3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("18", a3)
print("19", a3.shape) #(3,4)
print("20", a3.ndim)    #2
# print("21", a3.dtype.name)
# print("22", a3.itemsize)
# print("23", a3.size)
# print("24",  type(a3))

