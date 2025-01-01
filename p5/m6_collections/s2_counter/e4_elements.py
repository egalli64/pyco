"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

Counter - elements
"""

from collections import Counter

s = "welcome to python world"
print(f"The orginal string: '{s}'")

counter = Counter(s)
print(counter)

print("Elements", end=": ")
for cur in counter.elements():
    print(f"'{cur}'", end=" ")
