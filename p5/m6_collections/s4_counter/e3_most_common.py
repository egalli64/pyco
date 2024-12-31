"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 6 - The collections module

Counter - most common
"""

from collections import Counter

s = "welcome to python world"
counter = Counter(s)

# three most common elements (characters) in s
top_three = counter.most_common(3)
print()
print(f"The three most common letters in '{s}' are:")
for cur in top_three:
    print(cur)

# all the tuples listed in descending order of counter
by_counter = counter.most_common()
print("Order by most common:", by_counter)
