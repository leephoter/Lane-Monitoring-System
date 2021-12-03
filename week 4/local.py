a = 0

def f1(b):
    print('hi 1 : ', b)
    b = 100
    print('hi 2 : ', b)
    global a
    a = 1000

f1(a)
print('hi 3 : ', a)
