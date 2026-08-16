#Question based on creating a dictionary and applying some methods
'''Create a dictionary of three friends and their phone numbers. Use:
keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them'''
a= {"abhinav": 1010101010 ,"rahul":2020202020, "messi":201420222026}
print(a.keys())
print(a.values())
for name,number in a.items():
    print(name, number)