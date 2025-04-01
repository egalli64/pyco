"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

Counter - on a list
"""

from collections import Counter

fruits = ["orange", "apple", "banana", "apple", "banana", "apple"]
print("The list:", fruits)

counter = Counter(fruits)

# for readability, the Counter representation is in descending order by count
print(f"Counting the fruits: {counter}\n")

# but the order is not in the dictionary itself!
print("Looping on the counter")
for k, v in counter.items():
    print(f"k={k}: v={v}")
print()

# Counter is a dictionary, accessing its elements by []
print("How many oranges?", counter["orange"])
print("How many strawberries?", counter["strawberry"])
