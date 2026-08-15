#Learning docstrings- writing function documentation
def add(a,b):
    '''this fxn gives result of sum of two numbers'''
    return a+b
print(add.__doc__)


def add(a,b):
    '''
    Returns the sum of two numbers
    
    Parameters:
    a(int): The first number
    b(int): The second numer
    
    returns:
    int: The sum of two numbers
    '''
    return a+b    
print(add.__doc__)