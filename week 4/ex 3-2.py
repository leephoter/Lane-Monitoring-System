import math

n = int(input("number? "))
max = (int)((n-1) / 2)
for line in range(n) :
    blank = max - abs(max - n)
    for j in range(blank):
        print(" ",end='')
    print("*****")