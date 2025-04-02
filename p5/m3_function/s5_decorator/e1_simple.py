"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - An example
"""


def decorator(decorated):
    """Generate a function that wraps the passed argument"""

    def wrapper(*args, **kwargs):
        """Capture the decorated function and wrap it with extra code"""
        print("Before the actual function call")
        result = decorated(*args, **kwargs)
        print("After the actual function call")
        return result

    return wrapper


@decorator
def hello(name):
    print("Hello,", name)


print("Invoking the decorated function ...")
hello("Alice")
