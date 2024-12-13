"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Module

A "main" module
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
