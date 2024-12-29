"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

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
