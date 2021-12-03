str = input("문자열을 입력하세요")
n = len(str)
for i in range(n):
    for j in range(i+1):
        print(str[i], end='')
    print("")