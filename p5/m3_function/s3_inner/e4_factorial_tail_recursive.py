"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Factorial function - tail recursive (no inner function)
"""


def factorial(n, accumulator=1):
    """Tail recursive implementation - exposing the accumulator to the caller"""
    if n == 0:
        return accumulator
    else:
        return factorial(n - 1, n * accumulator)


print("Factorial of 7 (tail recursive):", factorial(7))
