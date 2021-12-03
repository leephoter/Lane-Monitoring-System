iStr = input("input string? ")

length = len(iStr)
sumCount = 0
cmpChr = 'a'
count = 0
alpha = []
alphaCount = []

while sumCount < length:
    for i in range(length):
        if iStr[i]==cmpChr:
            count += 1
    if count>0 :
        sumCount += count
        alpha.append(cmpChr)
        alphaCount.append(count)
    if cmpChr=='z':
        cmpChr = 'A'
    else:
        cmpChr = chr( ord(cmpChr)+1 )
    count = 0

for i in range(len(alpha)):
    print(alpha[i], " : ", alphaCount[i])
