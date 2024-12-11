"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

More shallow copy
"""

red = {"kim": [1284, 2312], "bob": []}
print("The red team:", red)

# 2. shallow object copy by ctor
yellow = dict(red)

if id(yellow) != id(red):
    print("Shallow copy by dict(): two variables, two objects")
if id(yellow["kim"]) == id(red["kim"]):
    print("But values in the dictionary refer to the same object")

yellow["kim"][0] += 1
print(f"A change in the copy {yellow['kim']} is a change in the original {red['kim']}")

# 3. shallow object copy by dictionary comprehension
yellow = {k: v for k, v in red.items()}

if id(yellow) != id(red):
    print("Shallow copy by comprehension: two variables, two objects")
if id(yellow["kim"]) == id(red["kim"]):
    print("But values in the dictionary refer to the same object")

yellow["kim"][0] += 1
print(f"A change in the copy {yellow['kim']} is a change in the original {red['kim']}")
