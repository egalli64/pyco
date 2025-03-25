"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Shallow copy
"""

matrix = [[i + j for j in range(3)] for i in range(3)]
print("A matrix:", matrix, "\n")

# constructor
other = list(matrix)
print("A matrix copy (1 - constructor):", other)

other[0][1] = 42
print("A change in the copy:", other)
print("Affect also the original:", matrix, "\n")

# slicing
other_2 = matrix[:]
print("A matrix copy (2 - slicing):", other_2)

other_2[1][1] = 42
print("A change in the copy:", other_2)
print("Affect also the original:", matrix, "\n")

# copy()
other_3 = matrix.copy()
print("A matrix copy (3 - copy):", other_3)

other_3[2][1] = 42
print("A change in the copy:", other_3)
print("Affect also the original:", matrix)
