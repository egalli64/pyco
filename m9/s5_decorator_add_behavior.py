"""
Python Course

https://github.com/egalli64/pyco

Module 9 - More on functions

Decorator (add behavior to decorated function)
"""


def log_decorator(f):
    """A decorator to log on request"""

    def wrapper(*args, **kwargs):
        """The closure wraps the call to the decorated function"""
        # 1. before
        print(f"Calling {f.__name__} with {args} and {kwargs}")

        # 2. call the wrapped function
        result = f(*args, **kwargs)

        # 3. after
        print(f"{f.__name__} returned: {result}")
        return result

    return wrapper


@log_decorator
def adder(a, b):
    return a + b


@log_decorator
def multiplier(x, y):
    return x * y


# calling the decorated functions
print("The adding result is:", adder(23, 19))
print("The multiplying result is:", multiplier(y=6, x=7))
