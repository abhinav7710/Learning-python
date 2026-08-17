#Learning inheritance: building upon existance classes
class animal: #parent class
    location= "australia"
    def __init__(self, name):
        self.name= name
    def speak(self):
        print("speaking now...")

class dog(animal): #inheritance
    def speak(self):
        super().speak() #using the speak fxn of parent class
        print("woof")

a = animal("dog")
a.speak
d= dog("bruno")       
d.speak()
print(d.location)


