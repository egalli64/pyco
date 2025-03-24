"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

List comprehension - not using it
"""

# list of values in [1 .. 6]
xs = list(range(1, 7))
print("A list from a range:", xs)

# list of squares
squares = []
for i in range(1, 11):
    squares.append(i**2)
print("Populating a list with a for loop:", squares)
