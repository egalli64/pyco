"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

Counter - on a list
"""

from collections import Counter

fruits = ["orange", "apple", "banana", "apple", "banana", "apple"]
counter = Counter(fruits)

# for readability, printing the Counter we see the elements in descending order by count
print(counter)

# but the order is not in the dictionary itself!
for k, v in counter.items():
    print(f"k={k}: v={v}")
