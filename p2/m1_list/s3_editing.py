"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

List methods for editing
"""

friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)

# append a new element (at the end)
friends.append("joe")
print("After append:", friends)

# insert in the given position
friends.insert(3, "lee")
print("After insert at 3:", friends)

# extend with an iterable
new_friends = ("ada", "ben", "cho")
friends.extend(new_friends)
print("After extend:", friends)

# concatenation among different types doesn't compile
# friends = friends + ("dean", "emma", "fin")
# augmented concatenated assignment works alright
friends += "dean", "emma", "fin"
print("After concatenation:", friends)

# delete the element in a given position
del friends[-2]
print("After del at -2:", friends)

# pop the last element
popped = friends.pop()
print("The element popped:", popped)
print("After pop:", friends)

# pop in a given position
popped = friends.pop(1)
print("The element popped at position 1:", popped)
print("After pop:", friends)

# pop a bad index raises an IndexError
try:
    friends.pop(42)
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
