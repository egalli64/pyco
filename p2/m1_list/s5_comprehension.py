"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

List comprehension
"""

# list of values in [1 .. 6]
print("A list from a range:", list(range(1, 7)))


# list of squares
squares = []
for i in range(1, 11):
    squares.append(i**2)
print("Populating a list with a for loop:", squares)

# list comprehension

# worst than the list-range approach, actually
print("A simple but useless comprehension example:", [x for x in range(1, 7)])

# this one is more interesting
print("Compacting list creation and population in a comprehension:", [x**2 for x in range(1, 11)])

# filter to get only even numbers
print("A comprehension with conditional:", [x for x in range(10) if x % 2 == 0])

# the external comprehension for rows, the internal one for columns
matrix = [[i + j for j in range(2)] for i in range(3)]
print("A matrix by comprehension:", matrix)
