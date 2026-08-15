#Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers (method2)
def fibo(n, current=0, a=0, b=1):
    if n<= 0:
        return
    print(a, end=" ")

    fibo(n-1 ,current +1 , b, a+b)

a=int(input("Enter the number of terms of fibonacci series you want to print: "))
fibo(a)
print()