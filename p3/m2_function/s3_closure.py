"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - More on functions

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

print("Passing different values to the 'adder 12' closure:")
print("Argument 30:", adder_12(30))
print("Argument -7:", adder_12(-7))
