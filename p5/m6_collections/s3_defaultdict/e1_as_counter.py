"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

defaultdict - used as counter
"""

from collections import defaultdict, Counter

fruits = ["orange", "apple", "banana", "apple", "banana", "apple"]
print("A list of fruits:", fruits)

print("Counting with defaultdict")
counter = defaultdict(int)

for fruit in fruits:
    counter[fruit] += 1

for k, v in counter.items():
    print(f"Counter for {k} is {v}")

# Counter wins in this case
print("\nCounting with Counter")
counter = Counter(fruits)
for k, v in counter.items():
    print(f"Counter for {k} is {v}")
