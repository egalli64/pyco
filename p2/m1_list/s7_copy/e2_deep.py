"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Deep copy
"""

from copy import deepcopy

matrix = [[i + j for j in range(3)] for i in range(3)]
print("A matrix:", matrix)

other = deepcopy(matrix)
print("A matrix deepcopy:", other, "\n")

other[1][1] = 42
print("A change in the copy:", other)
print("Does not affect the original:", matrix)
