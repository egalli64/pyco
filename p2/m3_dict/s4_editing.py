"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Modify
"""

friends = {}
print("An empty dictionary:", friends)

# add two items
friends["jim"] = 9812
friends["tom"] = 3412
print("After adding jim and tom:", friends)

# edit a value
friends["jim"] = 1298
print("After changing jim value:", friends)

# setdefault won't modify an existing pair
cur_value = friends.setdefault("jim", 3874)
if cur_value != 3874:
    print("jim was already in friends")

# setdefault only insert a new pair
cur_value = friends.setdefault("dan", 3874)
if cur_value == 3874:
    print("Now dan is in friends")

# change and assign a value
try:
    # it works on existing pair
    friends["jim"] += 1
    print("After increasing jim value:", friends)

    # it throws a KeyError on a missing key
    friends["joe"] += 1
except KeyError as ex:
    print("Can't change value for the missing key", ex)

# remove items
try:
    # it works on existing pair
    del friends["jim"]
    print("After deleting jim:", friends)

    # it throws a KeyError on a missing key
    del friends["jim"]
except KeyError as ex:
    print("Can't delete item for the missing key", ex)

# pop items
try:
    # it works on existing pair
    value = friends.pop("tom")
    print("tom's value was", value)

    # it throws a KeyError on a missing key
    friends.pop("tom")
except KeyError as ex:
    print("Can't pop item for the missing key", ex)

# popitem
try:
    # it works on non-empty dictionary
    pair = friends.popitem()
    print("the most recently inserted pair was", pair)

    # it throws a KeyError on an empty dictionary
    friends.popitem()
except KeyError as ex:
    print("KeyError!", ex)

# remove all items
friends.clear()
print("After clearing friends:", friends)
