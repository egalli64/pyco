"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Inner function - An example
"""


def outer(x):
    def inner(y):
        return y * 2

    return inner(x)


print("Calling outer():", outer(5))

# the inner function can't be seen outside the function where it is defined
# inner(5)
