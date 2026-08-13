#Learning matchh case statements in python
a = int(input("enter a number between 0 to 10:"))
match a:
    case 2:
        print("you have won 7$")

    case 8:
        print("you have won 499 rupees")

    case 10:
        print("you have won a car")
    case _:
        print("better luck next time")


print("thanks for participating")        
        