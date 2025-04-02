"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - apply more than one decorator
"""


def alpha_decorator(func):
    """Append " alpha" to the decorated function result"""

    def wrapper(*args, **kwargs):
        print("Enter alpha wrapper")
        # call the next step in the pipeline (another decorator or the decorated function)
        result = func(*args, **kwargs) + " alpha"
        print("Exit alpha wrapper")
        # return to the previous decorator or to the caller
        return result

    return wrapper


def beta_decorator(func):
    """Append " beta" to the decorated function result"""

    def wrapper(*args, **kwargs):
        print("Enter beta wrapper")
        # call the next step in the pipeline (another decorator or the decorated function)
        result = func(*args, **kwargs) + " beta"
        print("Exit beta wrapper")
        # return to the previous decorator or to the caller
        return result

    return wrapper


# the execution pipeline starts here
@beta_decorator
@alpha_decorator
def echo(name):
    # the decorated function is called by the closest decorator
    print("The echo function")
    # return to the closest decorator
    return name


name = "Bob"
print("An alpha/beta decorated echo for", name)
print("The final result is:", echo(name))
