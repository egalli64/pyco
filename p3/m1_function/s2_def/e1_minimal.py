"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Definition and invocation: minimal functions
"""

try:
    minimal_function()
except NameError as e:
    print("Can't invoke a function before its definition")


def minimal_function():
    pass


# to invoke a function it should be already known to Python
minimal_function()


def minimal_function_with_docstring():
    """A minimal, do-nothing, documented function"""
    pass


minimal_function_with_docstring()

print("After invoking the do-nothing functions")
