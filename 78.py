#Learning classes and objects
class employee:
    company = "Asus"
    def get_salary(self):
    #self is important here because self is a way to reference the object of the class which is being created
     return 1250000

e1= employee() #an object of class employee is created here
print(e1.get_salary())  #employee e's get salary method is called
print(e1.company)
e2= employee()
print(e2.get_salary())
print(e2.company)

