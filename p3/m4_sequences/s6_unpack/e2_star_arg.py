"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Sequence

Unpacking
The * operator on arguments
"""
point = (53, 12)
print("my point is", point)

# star on arg
div, mod = divmod(*point)
print(f"{point[0]} // {point[1]} =", div)
print(f"{point[0]} % {point[1]} =", mod)
