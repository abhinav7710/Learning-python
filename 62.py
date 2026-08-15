#Common List Methods:
my_list = [1, 2, 3]

(my_list.append(4))
(my_list.insert(1, 99))
(my_list.remove(2))
print(my_list.pop())
(my_list.reverse())
(my_list.sort())

# List Comprehensions (Efficient List Creation)
squared = [x**2 for x in range(5)]
print(squared)