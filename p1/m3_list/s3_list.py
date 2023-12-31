"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 3 - List

List definition
"""
friends = ["bob", "tom", "kim"]

print("A list:", friends)
print("The list length is", len(friends))

first = friends[0]
print(f"The first friend is '{first}'")

last = friends[-1]
print(f"The last friend is '{last}'")

try:
    print(friends[42])
except IndexError:
    print("There is not an element with the passed index!")
