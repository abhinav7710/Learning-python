#Learning about global keyword
def sum(a,b):
    print("Sum of the numbers is: ")
    c= a+b
    global z #it will create a global variable instead of local variable
    z=91
    print(c)

z=3 #will not get assigned the value because global variable z is already defined
print(z)
sum(99,199)    

