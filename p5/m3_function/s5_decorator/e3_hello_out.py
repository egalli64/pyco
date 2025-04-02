"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - change result
"""


def uppercase_decorator(func):
    """Convert the result of the decorated method to uppecase"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def greet_generator(name):
    return f"Hello, {name}!"


name = "Bob"
print("Generate a uppercase-decorated greet for", name)
print(greet_generator(name))
