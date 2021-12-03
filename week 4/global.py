a = 0

def f1():
    global a

    print('hi 1 : ', a)
    a = 10
    print('hi 2 : ', a)

f1()
print('hi 3 : ', a)
