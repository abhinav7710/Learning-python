#Learning reduce
from functools import reduce
numbers = [22, 934, 8, 76, 92]
def sum(a, b):
    return a + b 

c = reduce(sum, numbers)
print(c)