"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Structured File

JSON - load
"""

import json

FILENAME = "friends.json"

# read friends to the passed JSON file
with open(FILENAME) as file:
    friends = json.load(file)
    for friend in friends:
        print(friend)
