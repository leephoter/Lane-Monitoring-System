a = 0

def f1():
    #a = 10
    b = -3   
    print(b)
    global a
    print('hi 1 : ', a)
    a = 100
    print('hi 2 : ', a)

f1()
print('hi 3 : ', a)
