#Learning lambda function
square = lambda x: x * x
print(square(4))

'''as good as writing
def square(x):
return x*x
'''
sum= lambda x,y: x+ y
print(sum(18,18))
'''as god as writing
def sum(x,y):
return x + y'''

numbers = [1,2,3,4]
squared = list(map(lambda x:  x**2, numbers))
print(squared)