#Learning about function scope and lifetime
def sum(a,b):
    c = a + b
    z=11 #local variable only for function and gets destroyed after function use
    return c

def greet():
    z=29 #another local variable
    print("hello")

z=22 #global variable
print(z)
print(sum(8,91))
greet()
