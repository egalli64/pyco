"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Generator and list comprehension
List comprehension for Cartesian product
"""

names = ["bob", "kim"]
colors = ["blue", "red", "green"]

print("Names:", names)
print("Colors:", colors)
print()

# 1. no comprehension
print("Cartesian product of names and colors (by for-in):")

couples = []
for name in names:
    for color in colors:
        couples.append((name, color))
print(couples)

# 2. comprehension
print(34 * " " + "(comprehension):")

couples = [(name, color) for name in names for color in colors]
print(couples)
