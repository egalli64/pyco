"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 2 - List

Definition
"""
friends = ["bob", "tom", "kim"]

print("A list:", friends)

first = friends[0]
print(f"The first friend is '{first}'")

last = friends[-1]
print(f"The last friend is '{last}'")

try:
    print(friends[42])
except IndexError:
    print("There is not an element with the passed index!")
