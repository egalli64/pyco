"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 6 - Sequence

Generator and list comprehension
List comprehension for Cartesian product
"""
names = ["bob", "kim"]
colors = ["blue", "red", "green"]

# cartesian product of names and colors
couples = [(name, color) for name in names for color in colors]
print(couples)

# same, by double for loop
couples = []
for name in names:
    for color in colors:
        couples.append((name, color))
print(couples)
