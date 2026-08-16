#Learning dictionaries and dictionary methods
#crreating a dictionary
student= {"name" : "abhinav", "age": 18, "grade": "A"}

#accessing and modifying values
print(student["name"])
student["age"]=22 #updating value
student["city"]= "new york"

#common dictionary methods
print(student.keys())
print(student.values())
print(student.items())
student.pop("age")
student.clear()

#dictionary comprehension
squares= {x: x**2 for x in range(5)}
print(squares)
