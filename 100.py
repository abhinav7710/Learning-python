#Using args and kwargs both
def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, abhinav=34, abhi=32, abhinav_kumar=31)