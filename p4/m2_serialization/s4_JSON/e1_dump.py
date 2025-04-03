"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

JSON - dump
"""

import json

PATH = "p4/m2_serialization/s4_JSON/"
FILENAME = PATH + "friends.json"

friends = [
    {"Name": "Tom", "Age": 42, "City": "Madrid"},
    {"Name": "Jenny", "Age": 37, "City": "Amsterdam"},
    {"Name": "Bob", "Age": 32, "City": "Paris"},
    {"Name": "Kim", "Age": 41, "City": "Stockholm"},
    {"Name": "Micky", "Age": 43, "City": "Berlin"},
    {"Name": "Lee", "Age": 38, "City": "London"},
]

# dump the object as a JSON string to file
with open(FILENAME, "w") as file:
    json.dump(friends, file)
