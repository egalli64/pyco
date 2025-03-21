"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Definition and invocation
"""

# NameError, can't invoke a function before its definition
# minimal_function()

# defining two functions


def minimal_function():
    pass


def minimal_function_with_docstring():
    """A minimal, do-nothing, documented function"""
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


# invoking the functions defined above
minimal_function()

minimal_function_with_docstring()

greeter("Tom")
