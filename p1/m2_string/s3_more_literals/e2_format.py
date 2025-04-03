"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

String literals: the format() method
"""

import math

radius = 5

# using the {} placeholder to format a string
print("The area of a circle with radius {} is {}".format(radius, math.pi * radius**2))

# the curly braces are normal characters in a normal string
print("This is an open curly brace '{' and this is a close one '}'")

# rounding
print("Rounding pi to the fifth decimal: {:.5f}".format(math.pi))

print("Dynamically set precision is handier with format() ...")
for i in range(5):
    print("{0:.{1}f}".format(math.pi, i))
