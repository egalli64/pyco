"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 2 - More on functions

Decorator (change input for and output from the decorated function)
"""


def increase_and_square(f):
    """
    A decorator that changes the arguments and result of the decorated function

    Each argument is increased by one
    The result is squared
    """

    def wrapper(*args, **kwargs):
        """The closure wraps the call to the decorated function"""
        # 1. before: increase of arguments
        increased_args = tuple(arg + 1 for arg in args)
        increased_kwargs = {key: value + 1 for key, value in kwargs.items()}
        print(f"The caller passed {args} and {kwargs} to {f.__name__}")
        print(f"The wrapper calls {f.__name__} with {increased_args} and {increased_kwargs}")

        # 2. call the wrapped function with increased arguments
        result = f(*increased_args, **increased_kwargs)

        # 3. after: square the result before returning
        squared_result = result**2
        print(f"{f.__name__} returns {result} to the wrapper")
        print(f"The wrapper changes the result to {squared_result} and return it")
        return squared_result

    return wrapper


@increase_and_square
def sum_and_multiply(a, b, c):
    """A simple function (decorated)"""
    return (a + b) * c


# calling the decorated function
print("The caller sees as result", sum_and_multiply(2, 3, c=4))
