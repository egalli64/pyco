"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - the operator []
"""

# a string is a sequence
str = "welcome to Python's world"
print("A string:", str, end="\n\n")

# the operator []
print(f"Its first char (index = 0) is '{str[0]}'")
print(f"Same (index = -len): '{str[-len(str)]}'")
print()

print(f"Its last char (index = -1) is '{str[-1]}'")
print(f"Same (len - 1): '{str[len(str) - 1]}'")
print()

try:
    print("The char at index 42 is:", str[42])
except IndexError as ex:
    print(ex)
