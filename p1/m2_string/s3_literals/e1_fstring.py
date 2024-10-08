"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

String literals
F-string
"""

PI = 3.141592653589793
radius = 5

# referring to variable / expression in a f-string
print(f"The area of a circle with radius {radius} is {PI * radius ** 2}")

# real number formatting
print(f"A pi approximation: {PI:.5f}")

# padding and alignment
print(f"Left aligned:  _{PI:<20}_")
print(f"Right aligned: _{PI:>20}_")
