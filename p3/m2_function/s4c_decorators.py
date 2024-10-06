"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - More on functions

Decorator - apply more than one decorator
"""


def increaser(f):
    """A decorator that increases arguments"""

    def increaser_wrapper(*args, **kwargs):
        # 1. increase the arguments
        increased_args = tuple(arg + 1 for arg in args)
        increased_kwargs = {key: value + 1 for key, value in kwargs.items()}
        print("increaser_wrapper calls the function", end=" ")
        print(f"with {increased_args} and {increased_kwargs}")

        # 2. call the wrapped function and return the result
        return f(*increased_args, **increased_kwargs)

    return increaser_wrapper


def squarer(f):
    """A decorator that squares the result"""

    def squarer_wrapper(*args, **kwargs):
        # 1. call the wrapped function
        result = f(*args, **kwargs)

        # 2. square the result before returning
        print(f"{f.__name__} returns {result} to the squarer_wrapper")
        return result**2

    return squarer_wrapper


@increaser
@squarer
def sum_and_multiply(a, b, c):
    return (a + b) * c


# calling the decorated functions
print("The caller sees as result", sum_and_multiply(2, 3, c=4))
