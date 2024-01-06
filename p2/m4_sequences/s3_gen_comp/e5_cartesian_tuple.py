"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Sequence

Generator and list comprehension
List comprehension for Cartesian product
"""
names = ["bob", "kim"]
colors = ["blue", "red", "green"]

# cartesian product of names and colors
couples = tuple((name, color) for name in names for color in colors)
print(couples)

# same, by double for loop
temp = []
for name in names:
    for color in colors:
        temp.append((name, color))
couples = tuple(temp)
print(couples)
