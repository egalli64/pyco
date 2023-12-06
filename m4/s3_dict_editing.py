"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 4 - Dictionary and set

Dictionary: insert, edit, remove, check
"""
friends = {}
print("An empty dictionary:", friends)

# add three items
friends["bob"] = 4423
friends["jim"] = 9812
friends["tom"] = 3412
print("After adding bob, jim, and tom:", friends)

# edit a value
friends["jim"] = 1298
print("After changing jim value:", friends)

# change and assign a value
try:
    friends["jim"] += 1
    print("After increasing jim value:", friends)
    friends["joe"] += 1
except KeyError:
    print("Can't change a value for a missing key!")

# remove items
try:
    del friends["jim"]
    print("After deleting jim:", friends)

    del friends["jim"]
except KeyError:
    print("Can't delete an item for a missing key!")

try:
    value = friends.pop("tom")
    print("tom's value was", value)

    friends.pop("tom")
except KeyError:
    print("Can't pop an item for a missing key!")

# check for presence
if "bob" in friends:
    print("bob is still in")

if "jim" not in friends:
    print("jim is not in anymore")
