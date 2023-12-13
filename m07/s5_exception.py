"""
Python Course

https://github.com/egalli64/pyco

Module 7 - Object Oriented Programming

Exception
"""


def raiser():
    """A function that always raise an exception"""
    raise NotImplementedError("Not yet implemented")


try:
    expected_result = raiser()
    print("I expected to get something in", expected_result)
except NotImplementedError:
    print("Someone raised an exception")
