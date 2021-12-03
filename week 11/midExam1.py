a = 1

while a <= 3:
    b = a
    c = a
    print("hi")
    while b < 3:
        while c < 10:
            print(c)
            if c >= 5:
                break
            c += 1
        b += c
    a += 1
print("bye")
