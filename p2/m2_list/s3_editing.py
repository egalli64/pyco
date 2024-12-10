"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 2 - List

List methods for editing
"""
friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)

# add 'joe' as new last element
friends.append("joe")
print("Appended joe:", friends)

# insert 'lee' at index 3
friends.insert(3, "lee")
print("Insert at 3:", friends)

friends.extend(("ada", "ben", "cho"))
print("Extended:", friends)

# concatenation among different types doesn't compile
# friends = friends + ("dean", "emma", "fin")
# augmented concatenated assignment works alright
friends += "dean", "emma", "fin"
print("Extended by concatenation:", friends)

# pop the second element from the end
del friends[-2]
print("After del at -2:", friends)

# po the last element in the list
popped = friends.pop()
print("Pop at the end:", popped)
print("After pop:", friends)

# po the second element from the list
popped = friends.pop(1)
print("Pop at position 1:", popped)
print("After pop:", friends)

# a bad index raises IndexError
try:
    friends.pop(42)
except IndexError as ex:
    print(ex)

# remove 'abe' from the list
friends.remove("abe")
print("After removing abe:", friends)

try:
    print("Trying to remove 'abe' a second time ...", end=" ")
    friends.remove("abe")
except ValueError as ex:
    print(ex, "... where x stands for 'abe'")
