"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments - Packing (and unpacking)
"""


def hello(title, name):
    """A simple function with two parameters"""
    print(f"Hello, {title} {name}!")


def greeting(*args):
    """A vararg function"""
    print("Hello", end=" ")
    if not args:
        print("stranger, ", end="")
    for name in args:
        print(f"{name}, ", end="")
    print("nice to meet you!")


# calling a vararg function
greeting("Tom")
greeting("Tom", "Bob")
greeting()


def print_info(name, **kwargs):
    """A keyword-vararg function"""
    if not kwargs:
        print("No info available for", name)

    for key, value in kwargs.items():
        print(f"{name} {key} is {value}")


# calling a keyword-vararg function
print_info("Tom", profession="coder", city="Madrid")
print_info("Bob")

# unpack an iterable argument to parameters
values = ("King", "James")
hello(*values)

# unpack a dictionary argument to parameters
info = {"title": "Mr", "name": "White"}
hello(**info)
