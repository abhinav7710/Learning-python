#Learning filters
# def sq_is_less_than(x)):
#     if x*x<100:
#         return True
#     else:
#         return False
a = [98, 3, 9, 23, 19, 66]

new = list(filter(lambda x: x*x<100, a))
print(new)