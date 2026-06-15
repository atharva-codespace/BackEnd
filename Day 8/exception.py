def add():
    try:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Addition of two numbers:",(a+b))
    except Exception as e:
        print(e)
    finally:
        print("program executed Successfully")


add()
