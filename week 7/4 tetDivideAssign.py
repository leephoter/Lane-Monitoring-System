no = 1000.0
while 1:
    try:
        a = float(input("input number? "))
    except:
        print("입력 오류!!")
        continue
    try:
        no = no / a
    except:
        print("조심!!")
    else:
        print(no)
    finally:
        print("bye")
