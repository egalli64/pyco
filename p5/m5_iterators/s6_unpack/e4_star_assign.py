"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Unpacking
The * operator for parallel assignment with values in excess
"""

xs = [1, 2, 3, 4]
print("Given a list:", xs)

a, b, *ys = xs
print(f"a={a}, b={b}, and ys={ys}")

a, *ys, b = xs
print(f"a={a}, ys={ys}, and b={b}")

*ys, a, b = xs
print(f"ys={ys}, a={a}, and b={b}")

a, b, c, d, *ys = xs
print(f"a={a}, b={b}, c={c}, d={d}, and ys={ys}")

# ValueError: not enough values to unpack (expected at least 5, got 4)
# a, b, c, d, e, *ys = xs
