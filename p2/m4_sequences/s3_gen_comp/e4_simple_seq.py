"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Sequence

Generator and list comprehension
Generator for tuple and array
"""
from array import array

# passing a generator to the tuple constructor
values = tuple(x for x in range(0, 100, 5) if x % 7 == 0)
print(values)

# passing a generator to the array constructor
values = array("I", (x for x in range(0, 100, 5) if x % 7 == 0))
print(values)
