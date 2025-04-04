"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Module

A module to be imported
"""

APPLICATION_NAME = "Skynet"


def greeting(name):
    """A simple function"""
    print(f"Hello, {name}! I'm {APPLICATION_NAME}")


if __name__ == "__main__":
    print("This file shouldn't be run as a script")
    greeting("Unknown")
