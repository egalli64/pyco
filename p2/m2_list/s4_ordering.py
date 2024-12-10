"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 2 - List

Ordering
"""
import random

friends = ["bobby", "ann", "kim", "li", "luc"]
print(f"Friends: {friends}\n")

# generate new lists, sorted copies of the original one
sorted_friends = sorted(friends)
print("Sorted friends:", sorted_friends)

reverse_sorted = sorted(friends, reverse=True)
print("Reversed sorted friends:", reverse_sorted)

sorted_friends = sorted(friends, key=len)
print("Friends sorted by len:", sorted_friends)
print(f"The original list: {friends}\n")

# sorting in-place
friends.sort()
print("In-place sorting:", friends)

# reverse sorting in-place by length
friends.sort(reverse=True, key=len)
print("In-place reverse sorting by len:", friends)

# shuffling
random.shuffle(friends)
print("Shuffled", friends)
