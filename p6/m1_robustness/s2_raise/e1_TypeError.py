"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Exception - raise
"""


def raiser(s):
    """A function that always raise an exception"""
    if type(s) != str:
        raise TypeError("A string was expected")
    else:
        print("The passed string is:", s)


# TypeError expected
raiser(42)

print("This statement should not be executed")
