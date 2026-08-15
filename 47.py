#Learning about modules and pip
print("in built modules")
import math
print(math.sqrt(16))

print("list of all in built modules - https://docs.python.org/2/py-modindex.html") 

print("external modules are second type of modules")

print("installing libraries from by running this command in terminal- python -m pip install requests")

import requests
r = requests.get("https://www.google.com")
print(r.text)
