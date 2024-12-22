"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - An example
"""


def simple_decorator(func):
    """Generate a function that wraps the passed argument"""

    def wrapper(*args, **kwargs):
        """it captures 'func' and wraps it with extra code"""
        print("Before the actual function call")
        result = func(*args, **kwargs)
        print("After the actual function call")
        return result

    return wrapper


@simple_decorator
def hello(name):
    print("Hello,", name)


print("Invoking the decorated function ...")
hello("Alice")
