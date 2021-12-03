#  -*- coding: utf-8 -*- 

alpha = raw_input("알파벳을 입력하세요 - ")
alphalist = list(alpha)
if len(alphalist)%2==0:
    print(alphalist[len(alphalist)/2-1], alphalist[len(alphalist)/2])
else:
    print(alphalist[len(alphalist)/2])

# if len(str1)%2 == 0:
#     print()

# num1 = int(input('첫번째 정수 !! : '))
# num2 = int(input('두번째 정수 !! : '))
# num3 = int(input('세번째 정수 !! : '))
# if num1%2==0:
#     num3=num3*2
# else:
#     num3=num3*3
# if num2%2==0 and num2%3==0:
#     print(num3*6)
# else:
#     print(num3*5)


# num1 = int(input('첫번째 정수 !! : '))
# num2 = int(input('두번째 정수 !! : '))
# num3 = int(input('세번째 정수 !! : '))
# new1 = abs(num1-num2)
# new2 = abs(num2-num3)
# new3 = abs(num1-num3)
# if new1 > new2:
#     if new1 > new3:
#         print(num1, num2)
#     else:
#         print(num1, num3)
# else:
#     if new2 > new3:
#         print(num2, num3)
#     else:
#         print(num1, num3)


# 1
# num = int(input('정수 입력 !! : '))
# if num%2==0 and num%7==0:
#     print("2와 7의 배수이네용 ㅎㅎ")
# else :
#     print("2와 7의 배수가 아닙니당!!")

