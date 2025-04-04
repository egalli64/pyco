"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

The unittest module - code to be tested
See the test package under pyco
From the project home run: python -m unittest discover test -t . -v
"""


def add(left, right):
    """An adder"""
    return left + right


def subtract(left, right):
    """A subtractor"""
    return left - right


def floor_divide(left, right):
    """A floor divider"""
    return left // right


if __name__ == "__main__":
    print("See tests")
