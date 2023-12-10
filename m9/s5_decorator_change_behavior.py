"""
Python Course

https://github.com/egalli64/pyco

Module 9 - More on functions

Decorator (change behavior of decorated function)
"""


def increase_and_square(f):
    """
    A decorator that changes the decorated behavior

    Each argument is increased by one
    The result is squared
    """

    def wrapper(*args, **kwargs):
        """The closure wraps the call to the decorated function"""
        # 1. before: in-place increase of arguments
        increased_args = tuple(arg + 1 for arg in args)
        increased_kwargs = {key: value + 1 for key, value in kwargs.items()}
        print(f"The caller passed {args} and {kwargs} to {f.__name__}")
        print(f"The wrapper calls it with {increased_args} and {increased_kwargs}")

        # 2. call the wrapped function with increased arguments
        result = f(*increased_args, **increased_kwargs)

        # 3. after: square the result before returning
        print(f"{f.__name__} returns {result} to the wrapper")
        return result**2

    return wrapper


@increase_and_square
def sum_and_multiply(a, b, c):
    return (a + b) * c


# calling the decorated functions
print("The caller sees as result", sum_and_multiply(2, 3, c=4))
