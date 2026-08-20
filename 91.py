#Learning exception handling
while True:
    try:
        a= int(input("enter number 1: "))
        b= int(input("enter number 2: "))
        print(f"the division is {a/b}")

    except ValueError:
        print("please don't do bad typecast")
    except ZeroDivisionError:
        print("don't divide by 0")
    except Exception as e:
        print("unknown error occured", e)            