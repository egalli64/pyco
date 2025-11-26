"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Module

Plain import of a module
"""

import a_module


def f():
    """A function defined in this module"""
    pass


if __name__ == "__main__":
    # calling a function defined in the current module
    f()

    # calling a function defined in the imported module
    a_module.greeting("Tom")

    # accessing a variable (constant) defined in the imported module
    print("The application name is", a_module.APPLICATION_NAME)
