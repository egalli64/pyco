"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments - parameter separator keyword only * (star)
"""


def greeting(salutation, *, title, name):
    """
    A simple function with three parameters

    The first argument can be passed by position or by keyword

    The other two only by keyword
    """
    print(f"{salutation}, {title} {name}!")


# no positional is OK
greeting(salutation="Good morning", title="Lady", name="Dahl")

# one positional is OK
greeting("Chop, chop", title="Sir", name="Pent")

try:
    # more than one positional won't work
    greeting("Welcome back", "Lady", "Dahl")
except TypeError as ex:
    print(ex)
