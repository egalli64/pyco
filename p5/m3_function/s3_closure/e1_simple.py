"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Closure - An example
"""


def outer(x):
    """Generate a function that multiply by x the passed argument"""

    def inner(y):
        """it captures 'x' and multiply it for its parameter"""
        return x * y

    return inner


by_five = outer(5)
print("Calling by_five(3):", by_five(3))
print("Calling by_five(7):", by_five(7))

# the inner function can't be seen outside the function where it is defined
# inner(5)
