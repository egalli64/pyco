"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Parameters and arguments - unpacking args
"""


def hello(title, name):
    """A simple function with two parameters"""
    print(f"Hello, {title} {name}!")


# a dictionary with keys matching with the parameter names
info = {"title": "Mr", "name": "White"}

try:
    # won't work, two arguments are expected
    hello(info)
except TypeError as e:
    print("TypeError ...", e)

# unpack a dictionary matching keys with the parameter names
hello(**info)

# a dictionary with keys not matching with the parameter names
info = {"title": "Sir", "surname": "Fleming"}

try:
    # won't work, two arguments are expected for the actual parameter names
    hello(**info)
except TypeError as e:
    print("TypeError ...", e)
