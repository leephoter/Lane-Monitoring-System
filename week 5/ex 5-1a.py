import math

num = [int(x) for x in input("n개의 수를 입력하세요.. ").split()]
length = len(num)
print("입력 갯수 : %d"%(length))
print(num)
a = s = length - 1
diff = []
for j in range(1, length):
    for i in range(j, length):
        diff.append(math.fabs((num[j-1])-num[i]))
print("diff : ",diff)

maxDiff = 0
maxIndx = 0
for i in range(len(diff)):
    if maxDiff<diff[i]:
        maxDiff = diff[i]
        maxIndx = i

while maxIndx>=s:
    a = a - 1
    s = s + a
print("maxDiff = ",maxDiff)
print("최대 차이나는 입력 수는 %d와 %d입니다."%(num[length - a - 1],num[length - s + maxIndx]))