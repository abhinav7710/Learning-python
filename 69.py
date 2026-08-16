#trying some basic questions based on lists

'''Create a list fruits = ["apple", "banana", "cherry"] .
Print the first fruit'''
fruits= ["apple", "banana", "cherry"]
print(fruits[0])
#Replace "banana" with "orange" .
index=fruits.index("banana")
fruits[index]="orange"
print(fruits)


#Print the length of the list.
print(len(fruits))

#Create a list of numbers from 1 to 10 .
a= ["1", "2","3", "4", "5", "6", "7", "8", "9", "10"]

#Print the first three numbers using slicing.
print(a[0:3])
#Print the last three numbers using slicing
print(a[7:10])