"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Factorial function - tail recursive with inner function
"""


def factorial(n):
    """Recursive implementation - the tail recursion kept as an implementation detail"""

    def tail_recursion(n, accumulator):
        """Inner function, the tail recursion, written in a compact way"""
        return accumulator if n == 0 else tail_recursion(n - 1, n * accumulator)

    return tail_recursion(n, 1)


print("Factorial of 7 (inner tail recursive):", factorial(7))
