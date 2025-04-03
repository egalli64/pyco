"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

pickle - dump
"""

import pickle

friends = [
    {"Name": "Tom", "Age": 42, "City": "Madrid"},
    {"Name": "Jenny", "Age": 37, "City": "Amsterdam"},
    {"Name": "Bob", "Age": 32, "City": "Paris"},
    {"Name": "Kim", "Age": 41, "City": "Stockholm"},
    {"Name": "Micky", "Age": 43, "City": "Berlin"},
    {"Name": "Lee", "Age": 38, "City": "London"},
]

with open("friends.pkl", "wb") as file:
    pickle.dump(friends, file)
