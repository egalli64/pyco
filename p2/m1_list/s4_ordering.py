"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Ordering
"""

import random

friends = ["bobby", "ann", "kim", "li", "luc"]
print(f"Friends: {friends}\n")

# generate new lists, sorted copies of the original one
xs = sorted(friends)
print("Sorted friends:", xs)

xs = sorted(friends, reverse=True)
print("Reversed sorted friends:", xs)

xs = sorted(friends, key=len, reverse=True)
print("Friends sorted by len:", xs)

# the original list has not changed
print(f"The original list: {friends}\n")

# sorting in-place
friends.sort()
print("In-place sorting:", friends)

# reverse sorting in-place by length
friends.sort(reverse=True, key=len)
print("In-place reverse sorting by len:", friends)

# shuffling in-place
random.shuffle(friends)
print("Shuffled:", friends)

# reverse the order in-place
friends.reverse()
print("Reversed:", friends)
