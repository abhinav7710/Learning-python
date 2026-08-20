#Learning kwargs
def trophies_as_captain(**kwargs):
    # kwargs is a dictionary with all pair values that are given
    for player in kwargs.keys():
        print(f"The trophies of {player} is {kwargs[player]}")

trophies_as_captain(Dhoni=5,Rohit=5,patidar =2, kohli=0)