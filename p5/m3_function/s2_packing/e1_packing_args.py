"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments - packing args
"""


def greeting(salutation, *args):
    """Packing arguments to args"""
    print(salutation, end=" ")
    if not args:
        print("stranger, ", end="")
    for name in args:
        print(f"{name}, ", end="")
    print("nice to meet you!")


try:
    # won't work
    greeting()
except TypeError as e:
    print("TypeError ...", e)

# no arg
greeting("Hello")

# one arg
greeting("Hello", "Tom")

# two args
greeting("Hi", "Tom", "Bob")

# three args
greeting("Hey", "Tom", "Bob", "Jim")
