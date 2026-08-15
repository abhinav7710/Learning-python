#Practicing a problem based on functions
'''Write a function safe_divide(a, b) that returns the result of a / b , but
returns "Cannot divide by zero" if b is 0 '''

def safe_divide(a, b):
    if b==0:
        return("Cannot divide by zero")
    return a/b

c= int(input("Enter the vale of dividend: "))
d= int(input("Enter the value of divisor: "))
print(safe_divide(c, d))