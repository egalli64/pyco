"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Parameters and arguments - packing args
"""


def greeting(salutation, *args):
    """Packing arguments to the tuple parameter args"""
    print(salutation, end=" ")

    if not args:
        # nothing provided as args, using a default value
        print("stranger, ", end="")
    for name in args:
        # using the provided variable number of arguments
        print(f"{name}, ", end="")

    print("nice to meet you!")


try:
    # won't work, at least an argument is expected
    greeting()
except TypeError as e:
    print("TypeError ...", e)

# no extra argument
greeting("Hello")

# one extra argument
greeting("Hello", "Tom")

# two extra arguments
greeting("Hi", "Tom", "Bob")

# three extra arguments
greeting("Hey", "Tom", "Bob", "Jim")
