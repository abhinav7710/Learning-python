#Learning args
def sum(*args): 
    # args will make tuple of all the values in sum
    total = 0
    for item in args:
        total += item 
    return total

print(sum(342, 2, 7, 9))