"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments - parameter separator positional only / (slash)
"""


def greeting(salutation, /, title, name):
    """
    A simple function with three parameters

    The first argument must be passed by position only

    The other two can be passed by position or by keyword
    """
    print(f"{salutation}, {title} {name}!")


# no by keyword is OK
greeting("Good morning", "Lady", "Dahl")

# first positional is OK
greeting("Chop, chop", title="Sir", name="Pent")

try:
    # first by keyword won't work
    greeting(salutation="Welcome back", title="Lady", name="Dahl")
except TypeError as ex:
    print(ex)
