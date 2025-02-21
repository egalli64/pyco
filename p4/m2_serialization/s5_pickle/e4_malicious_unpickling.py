"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

pickle - malicious load
"""

import pickle

with open("malicious.pkl", "rb") as file:
    malicious = pickle.load(file)

print(f"malicious is an innocent {malicious}, the system return value!")
