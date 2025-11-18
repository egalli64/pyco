"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

random: determinism by seed
"""

import random

random.seed(42)

print("Random float value in [0, 1):", random.random())
print("Random int value in [0, 9]:", random.randint(0, 9))
print("Random float value in [0, 9]:", random.uniform(0, 9))

names = ["Tom", "Bob", "Joe", "Kim", "Mae"]
print("A random name:", random.choice(names))
print("A random sample sized 2:", random.sample(names, 2))

random.shuffle(names)
print("Names after shuffling:", names)
