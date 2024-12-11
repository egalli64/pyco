"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Update
"""

# Given a dictionary
dx = {"a": 1, "b": 2}

print("The original dictionary:", dx)

# update by keyword argument
dx.update(c=3, a=9)
print("After update with keyword argument:", dx)

# update with another dictionary
dx.update({"d": 4, "b": 8})
print("After update with another dictionary:", dx)

# update with an iterable of tuples
dx.update((("e", 5), ("c", 7)))
print("After update with an iterable of tuples:", dx)
