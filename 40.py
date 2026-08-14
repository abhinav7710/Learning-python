#Taking user input string and checking if it is a palindrome
a = input("Enter a string: ").lower()
if a==a[::-1]: 
  print("the given string is a palindrome")
else:
  print("It is not a palindrome")
