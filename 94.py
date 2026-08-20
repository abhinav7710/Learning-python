#Learning maps
numbers = [81, 76, 54, 32, 2011, 99]

def square(x):
    return x * x
 
new = list(map(square, numbers))
print(new)
