"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 5 - Function

The "main" module
"""
import other

APPLICATION_NAME = "Skynet"


def greeting(name):
    """A simple function"""

    print(f"Hello, {name}! I'm {APPLICATION_NAME}")


if __name__ == "__main__":
    name = input("What's your name? ")

    greeting(name)
    other.fun()

    print("See you")
