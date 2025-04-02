"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Factorial function - the iterative way (no inner function, no recursion)
"""


def factorial(n):
    """Iterative implementation"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("Factorial of 7 (iterative):", factorial(7))
