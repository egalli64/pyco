"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

JSON - loads
"""

import json

# Given a JSON string
s = """[
    {"Name": "Tom", "Age": 42, "City": "Madrid"},
    {"Name": "Jenny", "Age": 37, "City": "Amsterdam"},
    {"Name": "Bob", "Age": 32, "City": "Paris"},
    {"Name": "Kim", "Age": 41, "City": "Stockholm"},
    {"Name": "Micky", "Age": 43, "City": "Berlin"},
    {"Name": "Lee", "Age": 38, "City": "London"}
]"""

print(f"The JSON string: {s}\n")

# load the JSON string into an object
friends = json.loads(s)
print(f"The deserialized list of friends: {friends}")

# use the object accordingly to its nature
print("Looping on friends:")
for friend in friends:
    print(friend)
