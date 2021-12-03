import math

num = [int(x) for x in input("n개의 수를 입력하세요.. ").split()]
length = len(num)
print("입력 갯수 : %d" %(length))
print(num)

diffMax = 0
for i in range(0, length-1):
    for j in range(i+1, length):
        diff = math.fabs(num[i]-num[j])
        if(diffMax< diff ):
            diffMax = diff
            s1 = i
            s2 = j
print("maxDiff = ",diffMax)
print("최대 차이나는 입력 수는 %d와 %d입니다."%(num[s1],num[s2]))