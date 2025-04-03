"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

JSON - dumps
"""

import json

friends = [
    {"Name": "Tom", "Age": 42, "City": "Madrid"},
    {"Name": "Jenny", "Age": 37, "City": "Amsterdam"},
    {"Name": "Bob", "Age": 32, "City": "Paris"},
    {"Name": "Kim", "Age": 41, "City": "Stockholm"},
    {"Name": "Micky", "Age": 43, "City": "Berlin"},
    {"Name": "Lee", "Age": 38, "City": "London"},
]

# dump the object into a JSON string
s = json.dumps(friends)
print(s)
