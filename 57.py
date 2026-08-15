#Practicing a question based on docstrings
'''Write a function multiply(a, b) that has a proper docstring explaining what
it does. Then use help(multiply) to display the docstring'''

def multiply(a, b):
    '''Returns the product of two numbers
    
    Parameters:
    a(int):The first number
    b(int): The second number
    
    Returns:
    int: The product of the two numbers
    '''
    return a*b
print(multiply(5,4))
help(multiply)