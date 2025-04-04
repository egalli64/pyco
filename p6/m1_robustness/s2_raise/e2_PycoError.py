"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Exception - raise
"""


class PycoError(Exception):
    """A Pyco specific exception"""


def raiser(value):
    """A function that always raise an exception"""
    if value != 42:
        raise PycoError(f"Don't know what to do with {value}")
    else:
        print(f"Using {value} to produce the solution")


# PycoError expected
raiser(24)

print("This statement should not be executed")
