"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Unpacking - Parallel assignment and swap
"""

# 1. unpacking a list
xs = [1, 2, 3, 4]
print("Given a list:", xs)

# each element should be assigned to a variable
a, b, c, d = xs
print(f"Unpack it in a={a}, b={b}, c={c}, and d={d}")

# 2. unpacking a tuple
point = (53, 12)
print("Given a tuple:", point)

x, y = point
print(f"Unpack it in x={x}, and y={y}")

# 3. swap
x, y = y, x
print(f"Swap: x={x}, and y={y}")
