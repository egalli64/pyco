"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Sequence

Generator and list comprehension
List comprehension for identity matrix
"""
RANK = 3

# create an identity matrix by list comprehension
identity = [[1 if i == j else 0 for j in range(RANK)] for i in range(RANK)]
print(identity)

# same, by double for loop
identity = []

for i in range(RANK):
    row = []
    for j in range(RANK):
        row.append(1 if i == j else 0)
    identity.append(row)
print(identity)
