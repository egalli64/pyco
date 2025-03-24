"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

List comprehension
"""

# worst than the list-range approach, actually
xs = [x for x in range(1, 7)]
print("A simple but useless comprehension example:", xs)

# this one is more interesting
squares = [x**2 for x in range(1, 11)]
print("Compacting list creation and population in a comprehension:", squares)
