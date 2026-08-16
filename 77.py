#Trying some quesions based on data structures
#Write a program that takes a list of numbers and removes all duplicates using a set.
numbers=[1,2,3,4,4,5,6,5,3,2]
unique_no =set(numbers)
print(unique_no)

#Given a dictionary of products and their prices, find the product with the highest price.
products ={
    "Laptop": 160000,"phone": 39000,"headphoes": 7999}
highest= max(products,key=products.get)
print(products[highest])

#Write a program that merges two dictionaries into one
dict1= {"name": "abhinav", "age": 18}
dict2={"city": "dehradun", "course": "B.Tech"}
merged={**dict1, **dict2}
print(merged)


