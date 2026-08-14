'''Write a program that keeps asking the user to enter a password until they
enter the correct one.'''
password = "Abhinav"
print("you have 5 attempts to unlock the portal with your password")
no_of_attempts = 0
while no_of_attempts < 6:
   no_of_attempts+=1
   enter_pass = input("Enter your password ")
   if enter_pass == password:
     print("You are welcome")
     break
   elif enter_pass != password:
     print("wrong password entered, try again and number of attempts remaining is: ", 5-no_of_attempts) 

