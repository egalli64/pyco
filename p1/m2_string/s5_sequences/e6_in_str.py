"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - in operator
"""

# a string is a sequence
str = "welcome to Python's world"
print("A string:", str, end="\n\n")

# operator (not) in
if "elc" in str:
    print("'elc' is in")
else:
    print("Unexpected!")

if "k" not in str:
    print("'k' is not in")
else:
    print("Unexpected!")
