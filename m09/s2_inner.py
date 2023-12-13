"""
Python Course

https://github.com/egalli64/pyco

Module 9 - More on functions

Inner function
"""


def factorial(n):
    """Simple implementation"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("Factorial of 7 (iterative):", factorial(7))


def factorial_recursive(x):
    """Plain recursive implementation"""
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("Factorial of 7 (plain recursive):", factorial_recursive(7))


def factorial_tail_recursive(n, accumulator=1):
    """Tail recursive implementation - exposing the accumulator to the caller"""
    if n == 0:
        return accumulator
    else:
        return factorial_tail_recursive(n - 1, n * accumulator)


print("Factorial of 7 (tail recursive):", factorial_tail_recursive(7))


def factorial_inner_tail_recursive(n):
    """Recursive implementation - tail recursion is just an implementation detail"""

    def tail_recursion(n, accumulator):
        """Inner function, the tail recursion"""
        if n == 0:
            return accumulator
        else:
            return tail_recursion(n - 1, n * accumulator)

    return tail_recursion(n, 1)


print("Factorial of 7 (inner tail recursive):", factorial_inner_tail_recursive(7))
