#Learning finally
a= int(input("enter number 1: "))
b = int(input("enter number 2: "))
try:
    c= a/b
    print(c)
except Exception as e:
    print(e)
#will always get executed
finally:
    print("this is always being executed")    
