"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Ordering: the sort() method (in-place)
"""

friends = ["bobby", "ann", "kim", "li", "luc"]
print(f"Friends: {friends}\n")

# sorting in-place
friends.sort()
print("In-place sorting:", friends)

# reverse sorting in-place by length
friends.sort(reverse=True, key=len)
print("In-place reverse sorting by len:", friends)
