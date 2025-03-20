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

if id(friends) != id(others):
    print("The two variables reference two different objects")

if id(friends[0]) == id(others[0]):
    print("But the elements are referring to the same objects!")
