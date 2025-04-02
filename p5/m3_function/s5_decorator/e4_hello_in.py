"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - change arguments
"""


def uppercase_decorator(func):
    """Convert the argument to uppercase before calling the decorated method"""

    def wrapper(*args, **kwargs):
        upper_args = tuple(arg.upper() for arg in args)
        upper_kwargs = {key: value.upper() for key, value in kwargs.items()}
        return func(*upper_args, **upper_kwargs)

    return wrapper


@uppercase_decorator
def greet_generator(name):
    return f"Hello, {name}!"


name = "Bob"
print("Generate a uppercase-decorated greet for", name)
print(greet_generator(name))
