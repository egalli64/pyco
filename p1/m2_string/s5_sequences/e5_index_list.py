"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - index() on list
"""

# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]
print("A list:", lis, end="\n\n")

# looking for a value in a list
for target in {"tim", "zoe"}:
    print("Searching for", target, end=" ... ")
    try:
        pos = lis.index(target)
        print("found at", pos)
    except ValueError as ex:
        print(ex)
print()
