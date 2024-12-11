"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 2 - Tuple

Comprehension
"""

squared_evens = tuple(x**2 for x in range(10) if x % 2 == 0)
print("Not really a comprehension, but close enough:", squared_evens)
