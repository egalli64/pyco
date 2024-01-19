"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

String as sequence of characters
"""
s = "welcome to Python's world"

# the builtin len() at work on a string
print(f"The length of '{s}' is", len(s))

# the operator [] is defined for each sequence, so it works on strings too
print("The first char is:", s[0])
print("The char at index 12 is:", s[12])

try:
    print("The char at index 42 is:", s[42])
except IndexError:
    print("Beware of out of range indices!")
