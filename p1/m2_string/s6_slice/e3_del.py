"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - del on slice
"""
# a string is a sequence
str = "welcome to Python's world"
print("A string:", str)
# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]
print("A list:", lis)
print()

# strings are immutable sequences
try:
    del str[1:3]
except TypeError as ex:
    print(ex)

# lists are mutable sequences
del lis[1:3]
print("After slice del on the mutable sequence:", lis)

# wrong indices mean do not delete anything
del lis[42:25]
print("After wrong slice del on the mutable sequence (nothing to delete):", lis)
