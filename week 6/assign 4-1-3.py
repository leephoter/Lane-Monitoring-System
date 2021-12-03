data = input("string? ")

out =''
length  = len(data)
for i in range(length-1,-1,-1):
    out = out + data[i]
print(out)
