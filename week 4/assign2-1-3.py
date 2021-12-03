num1 = int(input("수를 입력하세요.. "))
num2 = int(input("수를 입력하세요.. "))
num3 = int(input("수를 입력하세요.. "))

if num1%2==0:
    num3 *= 2
else:
    num3 *= 3
if num2%2==0 and num2%3==0:
    num3 *= 6
else:
    num3 *= 5
print(num3)