# Modules and pip - Using External Libraries
'''
Importing Modules
Python provides built-in and third-party modules.

'''
# two type of modules:
# 1. Built-in Modules

# import math
# print(math.sqrt(16))  # Output: 4.0
# you can learn more about built in modules here: https://docs.python.org/3/py-modindex.html , or just simply search python built in modules


# we can also write our own modules and import them here
#  just see the mymodules.py file in this folder from where we are importing a function here
import mymodules
mymodules.great("Alice")  # Output: Hello, Alice!

# 2. External Modules (Third-party Modules), which we need to install using pip
# just write "pip install requests" in the terminal to install requests module

# import requests
 
# response = requests.get("https://api.github.com")
# print(response.status_code)

# you can learn more about requests module here: https://docs.python-requests.org/en/latest/
