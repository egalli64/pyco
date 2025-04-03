"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

String literals: F-string
"""

import math

radius = 5

# referring to variable / expression in a f-string
print(f"The area of a circle with radius {radius} is {math.pi * radius ** 2}")

# to print a curly brace in a f-string, just double it
print(f"This is an open curly brace '{{' and this is a close one '}}'")

# rounding
print("Rounding pi to the fifth decimal: {math.pi:.5f}")

print("Dynamically set precision is clumsy with f-strings ...")
for i in range(5):
    precision = f".{i}f"
    print(f"{math.pi:{precision}}")
