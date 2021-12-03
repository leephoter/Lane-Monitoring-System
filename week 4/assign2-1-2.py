import math

num1, num2, num3 = [int(x) for x in input("3개의 수를 입력하세요.. ").split()]
# 인수 x를 
print("%d %d %d"%(num1, num2, num3))
print(num2)

arr1 = [0 for i in range(10)]
print(arr1)

# diff1 = math.fabs(num1-num2)
# diff2 = math.fabs(num2-num3)
# diff3 = math.fabs(num3-num1)

# if diff1 < diff2:
#     if diff2 < diff3:
#         print(num1, num3)
#     else:
#         print(num2, num3)
# else:
#     if diff1 < diff3:
#         print(num1, num3)
#     else:
#         print(num1, num2)
