"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

Math: some more advanced math functions
"""

import math

n = 5

print("Factorial:")
for i in range(n):
    print(f"{i}! == {math.factorial(i)}")

print("\nCombination:")
for k in range(n + 1):
    print(f"Choose {k} items from {n} items -> {math.comb(n, k)}")

print("\nPermutation:")
for k in range(n + 1):
    print(f"Choose {k} items from {n} items (order matters) -> {math.perm(n, k)}")

print("\nBuilt-in abs:", abs(-1), abs(-2.0), abs(False))
print("Math float-abs:", math.fabs(-1), math.fabs(-2.0), math.fabs(False))
