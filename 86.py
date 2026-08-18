#Learning decorator
def decorator(func):
    def wrapper():
        print("i'm going to execute a fxn")
        func()
        print("i have executed the function")
    return wrapper
@decorator
def say_hello():
        print("hello")

say_hello()