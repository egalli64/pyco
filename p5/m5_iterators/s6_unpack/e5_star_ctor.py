"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Unpacking
The * operator in constructors
"""

a = (42, *range(3), 12)
print("A tuple:", a)

b = [42, *range(3), 12]
print("A list:", b)

c = {42, *range(3), 12}
print("A set:", c)
