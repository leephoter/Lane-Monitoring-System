iStr = input("input string? ")

length = len(iStr)
sumCount = 0
cmpChr = 'a'
count = 0
alpha = []
alphaCount = []
maxCount = 0

while sumCount < length:
    for i in range(length):
        if iStr[i] == cmpChr:
            count += 1
    if count > 0:
        if maxCount<count:
            maxCount = count
        sumCount += count
        alpha.append(cmpChr)
        alphaCount.append(count)
    if cmpChr == 'z':
        cmpChr = 'A'
    else:
        cmpChr = chr(ord(cmpChr)+1)
    count = 0

for i in range(maxCount,0,-1):
    for j in range(len(alpha)):
        if alphaCount[j]>=i:
            print(alpha[j],end='')
        else:
            print(" ",end='')
    print("")