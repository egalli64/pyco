"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Generator

Generator function
"""


def even_squared(begin=0, end=10):
    """A generator function, returning the square of even values in [begin .. end)"""
    current = begin if begin % 2 == 0 else begin + 1
    for n in range(current, end, 2):
        yield n**2


# Iterate on the generator
print("Even squared in [0 .. 10)", end=": ")
for cur in even_squared():
    print(cur, end=" ")
print()

# Using another generator on a different interval
print("Even squared in [-3 .. 8)", end=": ")
for cur in even_squared(-3, 8):
    print(cur, end=" ")
print()
