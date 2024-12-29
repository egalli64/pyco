"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Generator and list comprehension
Compare list comprehension vs initialization by for loop
"""

# 1. List the squares of even numbers in a given range
print("Squares of even numbers in range(10), by for-in", end=": ")

# 1a. by looping
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)
print(squares)

# 1b. by comprehension
print(31 * " " + "by comprehension:", [x**2 for x in range(10) if x % 2 == 0])

# 2. List the values in a given range divisible by 5 and 7
print("Divisible by 5 and 7 in [0, 100), by for-in", end=": ")

# 2a. by looping
values = []
for x in range(0, 100, 5):
    if x % 7 == 0:
        values.append(x)
print(values)

# 2b. by comprehension
print(27 * " " + "by comprehension:", [x for x in range(0, 100, 5) if x % 7 == 0])
