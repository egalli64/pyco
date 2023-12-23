"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 3 - List

Editing
"""
friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)

# change the first element with 'bobby'
friends[0] = "bobby"
print("Changed element 0:", friends)

# be careful with index out of range
try:
    friends[42] = "crash"
except IndexError as ex:
    print("Trying to change element 42:", ex)

# add 'joe' as new last element
friends.append("joe")
print("Appended joe:", friends)

# insert 'lee' at index 3
friends.insert(3, "lee")
print("Insert at 3:", friends)

# remove the second element from the list
del friends[1]
print("After delete ad 1:", friends)

# remove the last element in the list
popped = friends.pop()
print("Popped at the end:", popped)
print("After pop:", friends)

# remove the second element from the list
popped = friends.pop(1)
print("Popped at position 1:", popped)
print("After pop:", friends)

# remove 'abe' from the list
friends.remove("abe")
print("After removing abe:", friends)

try:
    friends.remove("abe")
except ValueError as ex:
    print("_consider 'x' as 'abe' in the following message_", ex)
