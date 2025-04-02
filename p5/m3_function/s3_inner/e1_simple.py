"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Inner function - An example
"""


def outer(x):
    """A function"""

    def inner(y):
        """A function defined inside another function"""
        return y * 2

    # invoke the inner function and return its result
    return inner(x)


print("Calling outer():", outer(5))

# the inner function can't be seen outside the function where it is defined
try:
    inner(5)
except NameError as e:
    print("Can't see an inner function outside its definition scope:", e)
