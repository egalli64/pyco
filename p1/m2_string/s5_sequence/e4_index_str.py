"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequence - index()
"""

# a string is a sequence
str = "welcome to Python's world"
print("A string:", str, end="\n\n")

# looking for a substring in a string
for target in ("w", "wa"):
    print("Searching for", target, end=" ... ")
    try:
        pos = str.index(target)
        print("found at", pos)
    except ValueError as ex:
        print(ex)
print()
