no = 5
a = 3
while no > a:
    try: #무조건 실행
        a = a + 1
        print("a")
    except: #try 논리가 맞으면 실행 x
        print("b")
    else: #try 논리가 맞으면 실행 O
        print("c")
    finally: #마지막에 무조건 실행
        print("d")
