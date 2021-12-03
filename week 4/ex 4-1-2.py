import math

def printStar(a) :
    cen = a // 2
    for n in range(a) :
        for j in range(cen - abs(cen-n)):
            print(" ",end='')
        print("*****")

for i in range(3):
    a = int(input("number? "))
    printStar(a)
