"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Strings and variables

Sequences - del statement
"""
# a string is a sequence
str = "welcome to Python's world"
print("A string:", str)
# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]
print("A list:", lis)
print()

# strings are immutable sequences, do not support del on their elements
try:
    del str[2]
except TypeError as ex:
    print(ex)

# lists are mutable sequences, do support del on their elements
del lis[2]
print("After del on the mutable sequence:", lis)
