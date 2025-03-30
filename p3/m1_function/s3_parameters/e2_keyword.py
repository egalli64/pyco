"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Parameters and arguments - by keyword
"""


def greeting(title, name):
    """A simple function with two parameters"""
    print(f"Hello, {title} {name}!")


# same order - just document the arg to param association
greeting(title="Ms", name="Pat")

# different order - still works alright
greeting(name="Strange", title="Doctor")

# the first by position, the other by keyword
greeting("Ms", name="Pat")

# The Python parser generates a SyntaxError: positional argument follows keyword argument
# greeting(title="Ms", "Pat")
