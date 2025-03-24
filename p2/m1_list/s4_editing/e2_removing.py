"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Removing elements: pop(), del, remove(), clear()
"""

friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)

# pop the last element
popped = friends.pop()
print("The element popped:", popped)
print("After pop:", friends)

# pop in a given position
popped = friends.pop(1)
print("The element popped at position 1:", popped)
print("After pop:", friends)

# pop with a bad index raises an IndexError
try:
    friends.pop(42)
except IndexError as ex:
    print(ex)

# delete the element in a given position
del friends[-2]
print("After del at -2:", friends)

# delete with a bad index raises an IndexError
try:
    del friends[42]
except IndexError as ex:
    print(ex)

# remove 'abe' from the list
friends.remove("abe")
print("After removing abe:", friends)

# remove a bad value raises a ValueError
try:
    print("Trying to remove 'abe' a second time ...", end=" ")
    friends.remove("abe")
except ValueError as ex:
    print(ex, "... where x stands for 'abe'")

# make the list empty
friends.clear()
print("After clear:", friends)
