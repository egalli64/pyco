"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Check - case
"""

targets = ("a", "BB", "Aa Bb", "", "AB ab")

print("Is the target lowercase?")
for target in targets:
    print(f"'{target}':", target.islower())
print()

print("Is the target uppercase?")
for target in targets:
    print(f"'{target}':", target.isupper())
print()

print("Is the target titlecase?")
for target in targets:
    print(f"'{target}':", target.istitle())
print()
