"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 4 - Dictionary and set

Dictionary: insert, edit, remove, check
"""
friends = {}
print("An empty dictionary:", friends)

# add two pairs
friends["bob"] = 4423
friends["jim"] = 9812
print("After adding bob and jim:", friends)

# edit a value
friends["jim"] = 1298
print("After changing jim value:", friends)

# change and assign a value
friends["jim"] += 1
print("After increasing jim value:", friends)

try:
    friends["tom"] += 1
except KeyError:
    print("Can't change a value for a missing key!")

# remove a pair
del friends["jim"]
print("After deleting jim:", friends)

try:
    del friends["tom"]
except KeyError:
    print("Can't delete a pair for a missing key!")

# check for presence
if "bob" in friends:
    print("bob is still in")

if "jim" not in friends:
    print("jim is not in anymore")
