no = 1000.0
while 1:
    a = float(input("input number? "))
    try:
        no = no / a
    except:
        print("조심!!")
    else:
        print(no)
    finally:
        print("bye")
