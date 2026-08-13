#writing a program that tells the user that given number as input is positive, negative or zero
a = int(input("Enter an integer: "))
if a > 0:
    print("The number is a positive integer")

elif  a == 0:
    print("The given integer is zero")
else:
    print("The given integer is negative")   