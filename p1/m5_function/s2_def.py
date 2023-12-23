"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 5 - Function

Definition and invocation
"""

# NameError, can't invoke a function before its definition
# minimal_function()

# defining two functions


def minimal_function():
    """A minimal, do-nothing, function"""
    pass


def greeter(name):
    """
    Define a function named "greeter" that print a hello message to the passed name

    Parameters:
        name: a string, name of the greeted person

    Returns:
        None
    """
    print(f"Hello, {name}!")


# invoking the two functions above
minimal_function()
greeter("Tom")
