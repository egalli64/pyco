"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Unpacking
The * operator on parameter
"""


# packing arguments in excess in the last parameter
def f(a, b, *c):
    print(f"Three parameters: a={a}, b={b}, and starred c={c}")


# passing more arguments than the expected parameters, c is (3, 4)
f(1, 2, 3, 4)

# c is (3,)
f(1, 2, 3)

# c is ()
f(1, 2)

# TypeError: f() missing 1 required positional argument: 'b'
# f(1)
