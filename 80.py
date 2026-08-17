#Learning instance and class  attributes
class employee:
    company= "Asus" #class attribute
    def __init__(self, salary, name, bond, company):
        self.salary= salary #createan instance attribute of name of salary and assign it with salary
        self.name = name
        self.bond= bond
        self.company= company

    def get_salary(self):
            return self.salary

    def get_info(self):
         print(f"The name of the employee is {self.name} and salary is {self.salary}. the bond is for {self.bond} years")

e1= employee(34000, "joe", 4, "Tesla'")
print(e1.get_salary())
print(e1.get_info())
print(e1.company) #always prints instance attribute whenever present
print(employee.company)
#object introspection
print(dir(e1))