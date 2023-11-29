"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 5 - Function

Definition
"""

# NameError, can't invoke a function before its definition
# greeter("Bob")

# defining two functions


def minimal_function():
    """A minimal, do-nothing, function"""
    pass


def greeter(name):
    """
    Define a function named "greeter" that print a hello message to the passed name

    Parameters
    ----------
    name : a string
        The name object of greeting

    Returns
    -------
    None
    """
    print(f"Hello, {name}!")


# invoking the two functions above
minimal_function()
greeter("Tom")
