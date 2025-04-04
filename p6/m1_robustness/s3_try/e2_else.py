"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Exception - try / except / else
"""


def increase(value):
    """
    A function takes an int and return it increased

    It raises a TypeError if the passed argument is not an int
    """
    if type(value) != int:
        raise TypeError("An int was expected as argument")
    else:
        return value + 1


for x in "hello", 42:
    try:
        result = increase(x)
    except TypeError as e:
        print(f"Check '{x}' type:", e)
    else:
        print(x, "increased is", result)
