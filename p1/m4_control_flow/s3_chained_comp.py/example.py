"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Control Flow

Chained comparisons
"""

a = 3
b = 10

print(f"Given the interval [{a}..{b}], check if x is in it")
for x in (3, 7, 11):
    print("(plain) x is", x, end=": ")
    print(a <= x and x <= b, end="\t... ")

    print("(chained) x is", x, end=": ")
    print(a <= x <= b)
