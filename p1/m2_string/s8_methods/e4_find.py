"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Methods - find
"""

# The target string
s = "Welcome to Python"
print("The searched string:", s)
print()


for target in ("Python", "Java"):
    print(f"Find '{target}' in '{s}':", s.find(target))
