"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Generator and list comprehension
List comprehension for identity matrix
"""

RANK = 3

# 1. no comprehension
print("Indentity matrix (for-in)", end=": ")
identity = []

for i in range(RANK):
    row = []
    for j in range(RANK):
        row.append(1 if i == j else 0)
    identity.append(row)
print(identity)

# 2. comprehension

print(10 * " " + "(comprehension)", end=": ")
print([[1 if i == j else 0 for j in range(RANK)] for i in range(RANK)])
