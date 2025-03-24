"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Ordering: the sorted() built-in (copy)
"""

friends = ["bobby", "ann", "kim", "li", "luc"]
print(f"Friends: {friends}\n")

# generate new lists, sorted copies of the original one
xs = sorted(friends)
print("Sorted friends:", xs)

xs = sorted(friends, reverse=True)
print("Reversed sorted friends:", xs)

xs = sorted(friends, key=len, reverse=True)
print("Friends sorted by len:", xs)

print(f"The original list has not changed: {friends}\n")
