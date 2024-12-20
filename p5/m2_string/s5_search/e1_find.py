"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Search - find, rfind
"""

# The searched string
s = "Let Python be Python"

for target in ("Python", "Java"):
    print(f"Find '{target}' in '{s}':", s.find(target))
print()

for target in ("Python", "Java"):
    print(f"Reverse-find '{target}' in '{s}':", s.rfind(target))
