import math

while 1:
    k = int(input("number? "))

    center = k // 2
    for i in range(k):
        n = center - int(math.fabs(center-i))
        for j in range(n):
            print(" ",end='')
        for j in range(k):
            print("*",end='')
        print("")
