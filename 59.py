#Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

def fibo(n):
    if terms <=0:
        print("Enter a positive number")
        return
    print(f"The first {terms} fibonacci numbers are: ")
    for i in range(terms):
        print(fib(i), end= " ")
        print()
terms= int(input("Enter the number of terms of fibonacci series you want to print: "))
print(fibo(int(terms)))
