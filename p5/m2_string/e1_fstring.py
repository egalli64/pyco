"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Formatting f-string
"""

PI = 3.141592653589793
radius = 5

# referring to variable / expression in a f-string
print(f"The area of a circle with radius {radius} is {PI * radius ** 2}")

# rounding
print(f"A pi approximation: {PI:.5f}")

# padding and alignment
print(f"Left aligned:  _{PI:<20}_")
print(f"Right aligned: _{PI:>20}_")
print(f"Center aligned: _{PI:^20}_")
print()

# rounding, padding, alignment
print(f"Left aligned:  _{PI:<20.5}_")
print(f"Right aligned: _{PI:>20.5}_")
print(f"Center aligned: _{PI:^20.5}_")
