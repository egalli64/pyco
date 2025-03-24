"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

List comprehension - filter by if
"""

# filter to get only even numbers
even_squares = [x for x in range(10) if x % 2 == 0]
print("A comprehension with conditional:", even_squares)
