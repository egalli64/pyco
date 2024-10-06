"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - slice on list
"""
# a list
friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)
print()

# 'normal'
print("'Normal' slice [1..4):", end=" ")
print(friends[1:4])

# header
print("First three elements:", end=" ")
print(friends[:3])

# rest
print("After the third element:", end=" ")
print(friends[3:])

# tail
print("The last three elements:", end=" ")
print(friends[-3:])

# skip every second element
print("Alternate from first element:", end=" ")
print(friends[::2])

# skip every first element
print("Alternate from second element:", end=" ")
print(friends[1::2])

# no exception on slicing
print("Wrong interval, empty slice:", end=" ")
print(friends[42:18])
print()

# alias - different variables, same object
friends2 = friends
if friends is friends2 and friends == friends2:
    print("Alias: the object is the same")

# changing an element in the alias
friends2[0] = "bobby"
if friends[0] is friends2[0]:
    print("Alias: there is only one list, seen by two variables")

# object copy - different variables, different object
friends2 = friends[:]
if friends is not friends2 and friends == friends2:
    print("Copy: same values, two different lists")

# changing an element in the copy
friends2[-1] = "jean-luc"
if friends[-1] is not friends2[-1]:
    print("Copy: changes in a list are not seen by the other one")
