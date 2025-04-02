"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Parameters and arguments - unpacking args
"""


def hello(title, name):
    """A simple function with two parameters"""
    print(f"Hello, {title} {name}!")


# a tuple of strings
values = ("King", "James")

try:
    # won't work, two arguments are expected
    hello(values)
except TypeError as e:
    print("TypeError ...", e)

# unpack an iterable argument to parameters
hello(*values)

# a tuple of (too many) strings
values = ("King", "James", "III")
try:
    # won't work, two arguments are expected
    hello(*values)
except TypeError as e:
    print("TypeError ...", e)
