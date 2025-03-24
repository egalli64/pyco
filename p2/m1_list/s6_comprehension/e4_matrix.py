"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

List comprehension - matrix
"""

# the external comprehension for rows, the internal one for columns
matrix = [[i + j for j in range(2)] for i in range(3)]
print("A matrix by comprehension:", matrix)
