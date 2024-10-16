"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

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
print(f"After del on the mutable sequence: {lis}\n")

print("Be careful with index value:", end=" ")
try:
    del lis[42]
except IndexError as ex:
    print(ex)
