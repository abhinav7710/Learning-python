#Trying a question based on string formatting and f-strings
print("Using format() , create a sentence:'My name is John and I am 25 years old'")
print("by passing 'John' and 25 as variables")
name= "John"
age =25
print("My  name is {0} and I am {1} years old".format("John", "25"))


print("Do the same using f-strings")
print(f"My name is {name} and I am {age} years old")