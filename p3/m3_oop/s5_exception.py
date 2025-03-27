"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Object Oriented Programming

Exception
"""


def raiser():
    """A function that always raise an exception"""
    raise NotImplementedError("Not yet implemented")


try:
    expected_result = raiser()
    print("I expected to get something in", expected_result)
except NotImplementedError as ex:
    print("Exception:", ex)
else:
    print("No exception")
finally:
    print("In any case")
