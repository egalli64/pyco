"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 2 - List

Editing
"""
friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)

# change the first element with 'bobby'
friends[0] = "bobby"
print("Changed list:", friends)

# add 'joe' as new last element
friends.append("joe")
print("Changed list:", friends)

# insert 'lee' at index 3
friends.insert(3, "lee")
print("Changed list:", friends)

# remove the last element in the list
popped = friends.pop()
print("Removed:", popped)
print("Changed list:", friends)

# remove the second element from the list
popped = friends.pop(1)
print("Removed:", popped)
print("Changed list:", friends)

# remove the second element from the list
del friends[1]
print("Changed list:", friends)

# remove 'abe' from the list
friends.remove("abe")
print("Changed list:", friends)

try:
    friends.remove("billy")
except ValueError:
    print("Can't remove the specified element")
