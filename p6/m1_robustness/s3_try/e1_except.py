"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Exception - try / except
"""


def raiser():
    """A function that always raise an exception"""
    raise NotImplementedError("Not yet implemented")


try:
    expected_result = raiser()
    print("I expected to get something in", expected_result)
except NotImplementedError as ex:
    print("I've got a NotImplementedError:", ex)

print("Done")
