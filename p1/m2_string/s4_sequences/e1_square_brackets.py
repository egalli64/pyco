"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - the operator []
"""
# a string is a sequence
str = "welcome to Python's world"
# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]

# the builtin len() at work on sequences
print(f"The length of '{str}' is", len(str))
print(f"The length of '{lis}' is", len(lis))
print()

# the operator []
print(f"The first char in {str} (index = 0):", str[0])
print(f"\tsame (index = -len):", str[-len(str)])
print(f"The first element in {lis} (0):", lis[0])
print(f"\tsame (-len):", lis[-len(lis)])
print(f"The last char in {str} (-1):", str[-1])
print(f"\tsame (len - 1):", str[len(str) - 1])
print(f"The last element in {lis} (-1):", lis[-1])
print(f"\tsame (len - 1):", lis[len(lis) - 1])
print()

# a list of string is a sequence of sequences!
print(f"The first char in the first element of {lis} is:", lis[0][0])
print(f"The last char in the last element of {lis} is:", lis[-1][-1])
print()

try:
    print("The char at index 42 is:", str[42])
except IndexError as ex:
    print(ex)

try:
    print("The element at index 42 is:", lis[42])
except IndexError as ex:
    print(ex)
