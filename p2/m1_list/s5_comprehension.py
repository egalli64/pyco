"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

List comprehension
"""

# list of values in [1 .. 6]
xs = list(range(1, 7))
print("A list from a range:", xs)

# list of squares
squares = []
for i in range(1, 11):
    squares.append(i**2)
print("Populating a list with a for loop:", squares)

# list comprehension

# worst than the list-range approach, actually
xs = [x for x in range(1, 7)]
print("A simple but useless comprehension example:", xs)

# this one is more interesting
squares = [x**2 for x in range(1, 11)]
print("Compacting list creation and population in a comprehension:", squares)

# filter to get only even numbers
even_squares = [x for x in range(10) if x % 2 == 0]
print("A comprehension with conditional:", even_squares)

# the external comprehension for rows, the internal one for columns
matrix = [[i + j for j in range(2)] for i in range(3)]
print("A matrix by comprehension:", matrix)
