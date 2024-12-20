"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

F-string formatting - number
"""

import math

# rounding
print(f"A pi approximation: {math.pi:.5f}")

# padding and alignment
print(f"Left aligned:   _{math.pi:<21}_")
print(f"Right aligned:  _{math.pi:>21}_")
print(f"Center aligned: _{math.pi:^21}_")
print()

# rounding, padding, alignment, with given char padding
print(f"Left aligned:   {math.pi:_<21.5}")
print(f"Right aligned:  {math.pi:_>21.5}")
print(f"Center aligned: {math.pi:_^21.5}")
