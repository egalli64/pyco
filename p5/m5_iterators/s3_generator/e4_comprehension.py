"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Generator

Generator comprehension
"""

print("Comprehension (for-in)", end=": ")
for cur in (x**2 for x in range(10)):
    print(cur, end=" ")
print()

print("Comprehension (iterating)", end=": ")
gen = (x**2 for x in range(10))

while True:
    try:
        print(next(gen), end=" ")
    except StopIteration:
        print()
        break
