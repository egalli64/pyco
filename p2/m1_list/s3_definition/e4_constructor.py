"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Constructor
"""

# a list of names by literal definition
friends = ["bob", "tom", "kim"]
print("A list:", friends)

# a shallow copy of another list by constructor
others = list(friends)
print("Another list:", others)

# the copy creates a new list
if id(friends) != id(others):
    print("The two variables reference two different objects")

# but the elements are the same!
if id(friends[0]) == id(others[0]):
    print("But the elements are referring to the same objects!")

# comparing the two lists for equality gives True
if friends == others:
    print("The two list are equal")
else:
    print("Unexpected")

# Since the elements are here immutable values, it's OK sharing objects
friends[0] = "bobby"
print(f"After changing a reference in {friends}, {others} stays unchanged")

if friends != others:
    print("Now the two lists are different")
else:
    print("Unexpected")
