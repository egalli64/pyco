"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

defaultdict - used for two-level grouping
"""

from collections import defaultdict

fruits = ["orange", "apple", "banana", "apple", "banana", "apple"]
print("A list of fruits:", fruits)

mapper = defaultdict(lambda: defaultdict(int))

for fruit in fruits:
    mapper[len(fruit)][fruit] += 1

for length, fruits in mapper.items():
    print("Fruits with len", length)
    for name, count in fruits.items():
        print(f"\t{name} ({count})")
