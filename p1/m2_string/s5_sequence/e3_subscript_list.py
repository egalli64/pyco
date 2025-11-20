"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequence - the operator [] on list
"""

# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]
print("A list:", lis, end="\n\n") # same as: print(f"A list {lis}\n")

# the operator []
print(f"Its first element (index = 0) is '{lis[0]}'")
print(f"Same (index = -len): '{lis[-len(lis)]}'")
print()

print(f"Its last element (index = -1) is '{lis[-1]}'")
print(f"Same (len - 1): '{lis[len(lis) - 1]}'")
print()

# a list of string is a sequence of sequences!
print(f"The first char in the first element of {lis} is", lis[0][0])
print(f"The last char in the last element of {lis} is", lis[-1][-1])
print()

try:
    print("The element at index 42 is:", lis[42])
except IndexError as ex:
    print(ex)
