

def makeRevStr(text) :
    revText = []
    for i in range(len(text)) :
        if ord('Z') >= ord(text[i]) >= ord('A'):
            revText.append(chr(ord(text[i]) + 32 ))
        elif ord('z') >= ord(text[i]) >= ord('a'):
            revText.append(chr(ord(text[i]) - 32))
        else :
            revText.append(text[i])
    newText = ''.join(revText)
    return newText

for i in range(3):
    text = input("input string = ")
    newText = makeRevStr(text)
    print(newText)
