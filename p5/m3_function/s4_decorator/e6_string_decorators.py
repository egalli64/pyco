"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - apply more than one decorator (on string)
"""


def uppercase_decorator(func):
    """Convert the result of the decorated function to uppecase"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


def exclaim_decorator(func):
    """Append an exclamation mark to the decorated function result"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"

    return wrapper


@uppercase_decorator
@exclaim_decorator
def greet_generator(name):
    return f"Hello, {name}"


name = "Bob"
print("Generate a exclaim- and uppercase- decorated greet for", name)
print(greet_generator(name))
