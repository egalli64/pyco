"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Dis-ordering: shuffle()
"""

import random

friends = ["bobby", "ann", "kim", "li", "luc"]
print(f"Friends: {friends}\n")

# shuffling in-place
random.shuffle(friends)
print("Shuffled:", friends)
