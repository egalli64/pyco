"""
Python Course

https://github.com/egalli64/pyco

Module 9 - More on functions

Closure
"""


def adder(first):
    """Generate a closure, adder to the passed argument"""

    def add(second):
        """Accept the second operand and return the sum"""
        return first + second

    return add


# Create an adder closure based on 12
adder_12 = adder(12)
print("Adding 30:", adder_12(30))
print("Adding -7:", adder_12(-7))
