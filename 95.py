#Learning filters
# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
a = [98, 3, 9, 23, 19, 66]

new = list(filter(lambda x: x*x<100, a))
print(new)