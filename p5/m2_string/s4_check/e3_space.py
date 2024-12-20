"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Check - space / printable
"""

targets = ("\t\n ", "A €!", "")

print("Is the target space?")
for target in targets:
    print(f"'{target}':", target.isspace())
print()

print("Is the target printable (or empty)?")
for target in targets:
    print(f"'{target}':", target.isprintable())
print()
