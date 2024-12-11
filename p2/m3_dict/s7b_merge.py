"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Merge
"""

# Given some dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "a": 9}
d3 = {"e": 5, "b": 8}

# merge them in a new one
dx = d1 | d2 | d3

print(f"Merging {d1}, {d2}, {d3} in {dx}")

# merge using the unpacking operator
dy = {**d1, **d2, **d3}
print("Same, by unpacking", dy)
