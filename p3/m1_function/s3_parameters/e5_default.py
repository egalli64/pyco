"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments - default parameter
"""


def greeting(title, name="Bob"):
    """A simple function with two parameters, the second with a default"""
    print(f"Welcome, {title} {name}!")


# passing both required arguments
greeting("Mr", "Tom")

# letting the name as default
greeting("Doctor")

greeting(title="Sir")

try:
    greeting()
except TypeError as e:
    print("The first parameter should be provided ...", e)
