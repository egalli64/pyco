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


# Create an adder closure based on the passed argument
my_adder = adder(12)

print("Passing different values to 'my_adder' closure:")
print("Passing 30 ...", my_adder(30))
print("Passing -7 ...", my_adder(-7))
