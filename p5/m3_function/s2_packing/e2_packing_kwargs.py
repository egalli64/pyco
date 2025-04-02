"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Parameters and arguments - packing kwargs
"""


def print_info(name, **kwargs):
    """Packing arguments to the dictionary parameter kwargs"""

    if not kwargs:
        # nothing provided as kwargs, fallback to a default behavior
        print("No info available for", name)

    for key, value in kwargs.items():
        # using the provided variable number of keyword arguments
        print(f"{name} {key} is {value}")

    print("---")


try:
    # won't work, at least an argument is expected
    print_info()
except TypeError as e:
    print("TypeError ...", e)

# no extra argument besides name
print_info("Bob")

# one extra argument (by keyword) besides name
print_info("Kim", profession="coder")

# two extra arguments (by keyword) besides name
print_info("Tom", profession="coder", city="Madrid")
