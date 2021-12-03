import math

str = input("문자열을 입력하세요")
n = len(str)
for i in range(n-1):
    if( str[i]!=str[i+1] ):
        count = math.fabs(ord(str[i])-ord(str[i+1]))-1
    else:
        count = 0
    print(count)