#Trying a question based on inheritance
'''Create a base class Animal with a method sound() that prints "Some sound" .
Create a derived class Dog that overrides sound() to print "Bark!" .
Create an object of Dog and call sound()'''
class Animal:
    def sound(self):
        print("some sound")
class dog(Animal):
    def sound(self):
        return("Bark")
a1= dog()        
print(a1.sound())
