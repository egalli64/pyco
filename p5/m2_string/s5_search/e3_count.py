"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Search - count
"""

# The searched string
s = "Let Python be Python"

for target in ("Python", "Java"):
    print(f"Count of '{target}' in '{s}':", s.count(target))
