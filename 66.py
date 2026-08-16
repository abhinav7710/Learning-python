#Learning sets and set methods

#creating a set
s1={"abhinav", "asus", "rog strix"}

#can't access elements like tuples and lists

#key set methods
my_set={1,2,3,4,5}

print(my_set.add(6))
print(my_set.remove(2))
print(my_set.discard(10))
print(my_set.pop())

#Set operations
a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))