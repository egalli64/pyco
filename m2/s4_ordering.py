"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 2 - List

Ordering
"""
import random

friends = ["bobby", "ann", "kim", "li", "luc"]
print("Friends:", friends)

# generate a new list, sorted copy of the original one
sorted_friends = sorted(friends)
print("Sorted friends:", sorted_friends)
print("The original list:", friends)

sorted_friends = sorted(friends, key=len)
print("Friends sorted by len:", sorted_friends)

# sorting in-place
friends.sort()
print("In-place sorting:", friends)

# reverse sorting in-place by length
friends.sort(reverse=True, key=len)
print("In-place reverse sorting by len:", friends)

# shuffling
random.shuffle(friends)
print("Shuffled", friends)
