"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

defaultdict - used for grouping
"""

from collections import defaultdict

fruits = ["orange", "apple", "banana", "apple", "banana", "apple"]
print("A list of fruits:", fruits)

# using set to discard duplicates
by_len = defaultdict(set)

for fruit in fruits:
    by_len[len(fruit)].add(fruit)

for k, v in by_len.items():
    print(f"Fruits with length {k}: {v}")
