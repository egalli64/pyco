"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Search - index, rindex
"""

# The searched string
s = "Let Python be Python"

for target in ("Python", "Java"):
    try:
        print(f"Index of '{target}' in '{s}':", s.index(target))
    except ValueError as ex:
        print(f"'{target}' leads to ValueError: {ex}")
print()

for target in ("Python", "Java"):
    try:
        print(f"Reverse-index of '{target}' in '{s}':", s.rindex(target))
    except ValueError as ex:
        print(f"'{target}' leads to ValueError: {ex}")
