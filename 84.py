#Trying a question based on constructor
'''Create a class Person with a constructor ( __init__ ) that accepts name and age
as arguments and stores them as instance attributes.
Create an object and print the person's name and age.'''

class person:
    def __init__(self, name, age):
        self.name= name
        self.age = age
        print(f"The name of person is {name} and his age is {age}")
p1= person("Abhinav",18)
