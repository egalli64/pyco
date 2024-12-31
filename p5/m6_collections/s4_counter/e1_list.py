"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

Counter - on a list
"""

from collections import Counter

fruits = ["orange", "apple", "banana", "apple", "banana", "apple"]
counter = Counter(fruits)
print(counter)
