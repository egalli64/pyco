"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments - by position
"""


def greeting(title, name):
    """A simple function with two parameters"""
    print(f"Hello, {title} {name}!")


greeting("Mr", "Tom")

try:
    greeting("Tom")
except TypeError as e:
    print("Exact match in number expected ...", e)
