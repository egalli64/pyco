"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

check existence by (not) in operator
"""

# a set
letters = set("emanuele")
print("A set from an iterable:", letters)

# in
if "a" in letters:
    print("The element 'a' is in the set")
else:
    print("Unexpected")

# not in
if "b" not in letters:
    print("The element 'b' is not in the set")
else:
    print("Unexpected")
