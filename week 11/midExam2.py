import math

def prtStar(n):
    max = (int)((n-1) / 2)
    for line in range(n) :
        blank = max - abs(max - line)
        for j in range(blank):
            print(" ",end='')
        print("*****",end='')
        for b in range((max-blank)*2):
            print(" ",end='')
        print("*****")

n = int(input("number? "))
prtStar(n)