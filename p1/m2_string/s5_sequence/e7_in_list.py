"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequence - in operator for list
"""

# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]
print("A list:", lis, end="\n\n")

# operator (not) in
if "tom" in lis:
    print("'tom' is in")
else:
    print("Unexpected!")

if "zoe" not in lis:
    print("'zoe' is not in")
else:
    print("Unexpected!")
