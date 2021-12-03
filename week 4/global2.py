a = 0
b = 1

def f1(b):
    global a

    print('hi 1 : ', a, b)
    a = 10
    b = 1000
    print('hi 2 : ', a, b)

print(a, b)
f1(a)
print('hi 3 : ', a, b)
