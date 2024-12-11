"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Reference copy, shallow and deep copy
"""

from copy import deepcopy

red = {"kim": [1284, 2312], "bob": []}
print("The red team:", red)

# 1. reference copy
yellow = red
if id(yellow) == id(red):
    print("Reference copy: two variables, one object")

# 2. shallow object copy
yellow = red.copy()
if id(yellow) != id(red):
    print("Shallow copy: two variables, two objects")
if id(yellow["kim"]) == id(red["kim"]):
    print("But values in the dictionary refer to the same object")

yellow["kim"][0] += 1
print(f"A change in the copy {yellow['kim']} is a change in the original {red['kim']}")

# 3. deep object copy
yellow = deepcopy(red)
if id(yellow) != id(red):
    print("Deep copy: two variables, two objects")
if id(yellow["kim"]) != id(red["kim"]):
    print("And values in the dictionary refer to different objects")

yellow["kim"][0] += 1
print(f"A change in the copy {yellow['kim']} is not seen in the original {red['kim']}")
