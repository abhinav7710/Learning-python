#Building the understandng of function arguments and return values
print("POSITIONAL ARGUMENTS")
def sum(a,b):
    return(a+b)
print(sum(5,3))

print("DEFAULT ARGUMENTS")
def greet(name="ABHINAV"):
    return(f"Hello, {name}")
print(greet())

print("KEYWORD ARGUMENTS")
def student(name,age):
    print(f"name:{name}, age: {age}")
student(age=20, name="ABHINAV")          