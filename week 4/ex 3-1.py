text = input("input string = ")
revText = []

for i in range(len(text)) :
    if ord('Z') >= ord(text[i]) >= ord('A'):
        revText.append(chr(ord(text[i]) - ord('A') + ord('a') ))
    elif ord('z') >= ord(text[i]) >= ord('a'):
        revText.append(chr(ord(text[i]) -  ord('a') + ord('A')))
    else :
        revText.append(text[i])
newText = ''.join(revText)
print(revText)
print(newText)

