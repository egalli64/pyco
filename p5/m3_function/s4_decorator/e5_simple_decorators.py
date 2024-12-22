"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - apply more than one decorator
"""


def alpha_decorator(func):
    """Convert the result of the decorated function to uppecase"""

    def wrapper(*args, **kwargs):
        print("Enter alpha wrapper")
        result = func(*args, **kwargs) + " alpha"
        print("Exit alpha wrapper")
        return result

    return wrapper


def beta_decorator(func):
    """Append an exclamation mark to the decorated function result"""

    def wrapper(*args, **kwargs):
        print("Enter beta wrapper")
        result = func(*args, **kwargs) + " beta"
        print("Exit beta wrapper")
        return result

    return wrapper


@beta_decorator
@alpha_decorator
def echo(name):
    print("The echo function")
    return name


name = "Bob"
print("An alpha- beta- decorated echo for", name)
print("The final result is:", echo(name))
