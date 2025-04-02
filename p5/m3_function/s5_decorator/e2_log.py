"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Decorator - add behavior for logging
"""


def log_decorator(func):
    """A decorator to add log before and after the calls to the decorated function"""

    def wrapper(*args, **kwargs):
        """The closure wraps the call to the decorated function"""
        # 1. before, log the input argument
        print(f"Calling {func.__name__} with arguments: {args} and {kwargs}")

        # 2. call the wrapped function
        result = func(*args, **kwargs)

        # 3. after, log the result
        print(f"{func.__name__} returned: {result}")
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
print("---")
print("The multiplying result is:", multiplier(y=6, x=7))
