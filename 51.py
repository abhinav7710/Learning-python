#Trying some questions on function arguments and values
'''Write a function full_name(first, last) that takes first name and last name " \
"as parameters and returns a single string in the format 'First Last'''

def full_name(first, last):
  first=  input("Enter your firt name: ")
  last=  input("Enter your second name: ")
  full= first + " "+ last
  print(full)

full_name("", "")

'''Write a function calculate_area(length, width=10) that returns the area of
a rectangle'''

def area(length):
  length = int(input("Enter the length of rectangle: "))
  area= length*10
  print("The area of the rectangle is: ", area)

area(9)