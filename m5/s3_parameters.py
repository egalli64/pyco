"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 5 - Function

Parameters - by position, by keyword, default
"""


def greeting(title, name):
    """A simple function with two parameters"""
    print(f"Hello, {title} {name}!")


# passing arguments by position
greeting("Mr", "Tom")

# passing arguments by keyword
greeting(title="Ms", name="Pat")
greeting(name="Strange", title="Doctor")


def greeting2(title, name="Bob"):
    """A simple function with two parameters, the second with a default"""
    print(f"Welcome, {title} {name}!")


# passing both required arguments
greeting2("Mr", "Tom")

# letting the name as default
greeting2("Doctor")


def greeting3(*names):
    print("Hello", end=" ")
    if len(names) == 0:
        print("stranger, ", end="")
    for name in names:
        print(f"{name}, ", end="")
    print("nice to meet you!")


greeting3("Tom")
greeting3("Tom", "Bob")
greeting3()
