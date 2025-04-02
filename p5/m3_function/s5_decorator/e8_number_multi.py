"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - More on functions

Decorator - apply more than one decorator (on numbers)
"""


def increaser(func):
    """A decorator that increases arguments"""

    def increaser_wrapper(*args, **kwargs):
        print(f"increaser_wrapper gets {args} and {kwargs}", end=" ")
        # 1. increase the arguments
        increased_args = tuple(arg + 1 for arg in args)
        increased_kwargs = {key: value + 1 for key, value in kwargs.items()}
        print(f"and pass in {increased_args} and {increased_kwargs}")

        # 2. call the wrapped function and return the result
        result = func(*increased_args, **increased_kwargs)
        print(f"increaser_wrapper gets {result} from {func.__name__}")
        return result

    return increaser_wrapper


def squarer(func):
    """A decorator that squares the result"""

    def squarer_wrapper(*args, **kwargs):
        # 1. call the wrapped function
        print(f"squarer_wrapper pass in {args} and {kwargs}")
        result = func(*args, **kwargs)

        # 2. square the result before returning
        print(f"squarer_wrapper gets {result} from {func.__name__}")
        result **= 2
        print("squarer_wrapper squares and return it")
        return result

    return squarer_wrapper


# in this case the decorator order is not relevant
@squarer
@increaser
def sum_and_multiply(a, b, c):
    return (a + b) * c


print("Invoking sum_and_multiply() from the global scope")
print("The caller sees as result", sum_and_multiply(2, 3, c=4))
