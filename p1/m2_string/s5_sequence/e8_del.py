"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Mutable sequence - del statement
"""

# a string is a sequence
str = "welcome to Python's world"
print("A string:", str)

# strings are immutable sequences, do not support del on their elements
try:
    del str[2]
except TypeError as ex:
    print(ex)

# lists are mutable sequences, do support del on their elements
lis = ["bob", "tom", "kim", "tim"]
print("\nA list:", lis)

del lis[2]
print("After deleting element in position 2:", lis)

print("\nBe careful with index value:", end=" ")
try:
    del lis[42]
except IndexError as ex:
    print(ex)
