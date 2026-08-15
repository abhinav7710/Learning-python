#Learning recursion in python
a= input("enter a number:")
def factorial(n):
  if n==1: #base value of recursion
   return 1
  return n* factorial(n-1)
print(factorial(int(a)))