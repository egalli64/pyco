"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Control Flow

Chained comparisons - monotonic triplet
"""

for xs in (3, 7, 8), (3, 8, 7), (7, 8, 9):
    print("(plain) {xs} is monotonic", end=": ")
    print(xs[0] <= xs[1] and xs[1] <= xs[2], end=" ... ")

    print("(chained)", end=": ")
    print(xs[0] <= xs[1] <= xs[2])
