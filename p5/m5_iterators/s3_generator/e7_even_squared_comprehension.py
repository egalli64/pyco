"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Generator

Using a generator by comprehension
"""

print("Even squared in [0 .. 10) by comprehension:", end=" ")
for cur in (n**2 for n in range(10) if n % 2 == 0):
    print(cur, end=" ")
print()

print("Even squared in [-3 .. 8) by comprehension:", end=" ")
for cur in (n**2 for n in range(-3, 8) if n % 2 == 0):
    print(cur, end=" ")
print()
