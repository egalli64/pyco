"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Closure - Adder example
"""


def adder(fixed):
    """Generate a closure, adder to the passed argument"""

    def add(second):
        """Accept the second operand and return the sum with the fixed one"""
        return fixed + second

    return add


# Create an adder closure based on 12
adder_12 = adder(12)

print("Passing different values to the 'adder 12' closure:")
print("Passing 30 ...", adder_12(30))
print("Passing -7 ...", adder_12(-7))
