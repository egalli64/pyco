"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - slice on tuple
"""

# a tuple
friends = ("bob", "tom", ["kim", "karen", "krug"], "abe", "luc")
print("A list:", friends)
print()

# A slice with start and stop: tom, [...]
print("Plain slice [1..3):", end=" ")
slice = friends[1:3]
print(slice)

# Can't assign a new reference to a tuple element
try:
    slice[0] = "tim"
except:
    print("Assign to a tuple leads to a TypeError")

# A list is mutable, even if it is defined in a tuple
slice[1][0] = "kimi"
print("Changing kim to kimi:", slice)
# Both friends and slice refer to the same object
print("The change is seen also in the original tuple!", friends[2])
