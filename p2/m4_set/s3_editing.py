"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Set: add, remove, ...
"""

# a set
friends = {"bob", "tom", "kim"}
print("Friends:", friends)

# add an element
friends.add("mia")
# no effect - duplicate is silently discarded
friends.add("bob")
print("Friends (add):", friends)

# update a set with an iterable, tom is not inserted being already in
others = ["tom", "zoe"]
friends.update(others)
print("Friends (update):", friends)

# remove an element, or throw a KeyError
try:
    friends.remove("tom")
    print("Friends (remove):", friends)
    friends.remove("tom")
except KeyError as ex:
    print("Can't remove a missing element:", ex)

# discard an element, or ignore the request
friends.discard("kim")
friends.discard("kim")
print("Friends (discard):", friends)

# pop an element (chosen by set)
print(friends.pop(), "was a friend (pop)")
print("Friends (pop):", friends)

# make the set empty
friends.clear()
print("Friends (clear):", friends)

# can't pop on an empty set
try:
    friends.pop()
except KeyError as ex:
    print("KeyError!", ex)
