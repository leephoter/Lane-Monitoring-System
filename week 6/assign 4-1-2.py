i1 = int(input("the first input number? "))
i2 = int(input("the second input number? "))
i3 = int(input("the third input number? "))

for n in range(1, i1+1):
    if n%i2==0 and n%i3==1:
        print(n," ",end='')