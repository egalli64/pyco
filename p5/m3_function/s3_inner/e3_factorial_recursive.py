"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Factorial function - recursive (no inner function)
"""


def factorial(x):
    """Plain recursive implementation"""
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("Factorial of 7 (plain recursive):", factorial(7))
