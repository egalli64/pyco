"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 6 - Sequence

Packing and unpacking
Parallel assignment and swap
"""
point = (53, 12)
print("My point is", point)

# unpacking
x, y = point
print(f"x is {x}, y is {y}")

# swap
x, y = y, x
print(f"After swap x is {x}, y is {y}")
