"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Definition and invocation: a hello function
"""


def hello(name):
    """
    Define a function named "hello" with this docstring that prints a hello message to the passed name

    Arguments:
        name: the greeted person (string)
    Returns:
        None
    """
    print(f"Hello, {name}!")


# invoking the function
hello("Tom")
