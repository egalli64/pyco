"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Sequence

Unpacking
The * operator in constructors
"""
a = (2, *range(3), 12)
print("A tuple:", a)

b = [2, *range(3), 12]
print("A list:", b)

c = {2, *range(3), 12}
print("A set:", c)
