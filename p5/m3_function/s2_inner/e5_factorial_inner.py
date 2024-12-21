"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Inner function - tail recursive
"""


def factorial(n):
    """Recursive implementation - tail recursion is just an implementation detail"""

    def tail_recursion(n, accumulator):
        """Inner function, the tail recursion"""
        if n == 0:
            return accumulator
        else:
            return tail_recursion(n - 1, n * accumulator)

    return tail_recursion(n, 1)


print("Factorial of 7 (inner tail recursive):", factorial(7))
