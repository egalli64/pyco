"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

random: on a sequence
"""

import random

names = ["Tom", "Bob", "Joe", "Kim", "Mae"]
print("A list of names:", names)

print("A random name:", random.choice(names))
print("A random sample sized 2:", random.sample(names, 2))

random.shuffle(names)
print("Names after shuffling:", names)
