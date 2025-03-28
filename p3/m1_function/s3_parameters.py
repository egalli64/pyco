"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments
"""


def greeting(title, name):
    """A simple function with two parameters"""
    print(f"Hello, {title} {name}!")


# passing arguments by position
greeting("Mr", "Tom")

# passing arguments by keyword
greeting(title="Ms", name="Pat")
greeting(name="Strange", title="Doctor")


def greeting_keyword_only(*, title, name):
    """
    A simple function with two parameters
    The argument can be passed only by keyword
    """
    print(f"Chop, chop, {title} {name}!")


greeting_keyword_only(title="Sir", name="Pent")
try:
    # won't work
    greeting_keyword_only("Lady", "Dahl")
except TypeError as ex:
    print(ex)


def greeting2(title, name="Bob"):
    """A simple function with two parameters, the second with a default"""
    print(f"Welcome, {title} {name}!")


# passing both required arguments
greeting2("Mr", "Tom")

# letting the name as default
greeting2("Doctor")


def greeting3(*args):
    """A vararg function"""
    print("Hello", end=" ")
    if not args:
        print("stranger, ", end="")
    for name in args:
        print(f"{name}, ", end="")
    print("nice to meet you!")


# calling a vararg function
greeting3("Tom")
greeting3("Tom", "Bob")
greeting3()


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
greeting(*values)
greeting3(*values)

# unpack a dictionary argument to parameters
info = {"title": "Mr", "name": "White"}
greeting(**info)
