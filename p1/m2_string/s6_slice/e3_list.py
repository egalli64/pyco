"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - slice on list
"""

# a list
friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)
print()

# A slice with start and stop: tom, kim
print("Plain slice [1..3):", end=" ")
slice = friends[1:3]
print(slice)

# A list is mutable, changing a reference in the slice ...
slice[0] = "tim"
print(slice)

# ... leaves the original sequence unchanged!
print("The change is not seen in the original tuple!", friends[1])
