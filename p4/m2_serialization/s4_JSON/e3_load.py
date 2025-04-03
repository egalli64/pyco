"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

JSON - load
"""

import json

PATH = "p4/m2_serialization/s4_JSON/"
FILENAME = PATH + "friends.json"

# load a JSON string from file to an object
with open(FILENAME) as file:
    friends = json.load(file)

print("The full list of friends:", friends)

# use the object accordingly to its nature
print("\nLooping on friends:")
for friend in friends:
    print(friend)
