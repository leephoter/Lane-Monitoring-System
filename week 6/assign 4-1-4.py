data = input("string? ")

out = ''
ch = 'a'
inLength  = len(data)
outLength = 0
while outLength < inLength:
    for i in range(inLength):
        if ch == data[i]:
            out += ch
            outLength += 1
    ch = chr(ord(ch) + 1)
print(out)