#Program to find nth term of fibonacci series
a= input("Enter a number: ")
def fib(n):
 if n == 0 or n == 1:
    return n
 return fib(n-2) + fib (n-1)
print(fib(int(a)))