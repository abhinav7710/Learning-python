#Trying some questions based on lambda function

#Write a lambda function that adds two numbers and test it
sum = lambda x,y: x + y
print(sum(5,3))

a= int(input("enter a number: "))
b= int(input("enter anoher number: "))
print(sum(a,b))





#Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares
numbers= [1,2,3,4,5]
squared= list(map(lambda x: x**2, numbers))
print(squared)
