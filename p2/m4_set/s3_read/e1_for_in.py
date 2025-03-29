"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Read access by for-in
"""

# an iterable (a string)
name = "emanuele"

# a set
letters = set(name)
print(f"A set {letters} generated from an iterable {name}")

# loop on it
print("Looping on the set:", end=" ")
for letter in letters:
    print(letter, end=" ")
print()
