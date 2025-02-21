"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

pickle - load
"""

import pickle

with open("friends.pkl", "rb") as file:
    friends = pickle.load(file)

for friend in friends:
    print(friend)
