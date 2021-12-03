while 1 :
    i1 = int(input("the first input number? "))
    i2 = int(input("the second input number? "))

    sum = 0
    n = 1
    while n*i2 <= i1:
        sum += n*i2
        n += 1
    print("sum = ",sum)
