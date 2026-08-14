#Learning about string formatting and f- strings 
name = "abhinav"
age=18
print("My name is {} and my age is {} years".format(name,age))

#specifying positional and keyword arguments
print("{name} is {age} years old".format(name= "abhinav kumar", age =18))
print("{0} is learning {1}".format("Abhinav", "python"))

#f-string (formated string literals)
print(f"my name is {name} and my age is {age} years old")

#using expression in f strings
x = 10
y=19
print(f"the sum of {x} and {y} is {x+y}")

#formating numbers
pi=3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")