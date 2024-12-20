"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Check - alpha-numeric
"""

targets = ("a", "c7", "42", "", "2?")

print("Is the target alpha-only and not empty?")
for target in targets:
    print(f"'{target}':", target.isalpha())
print()

print("Is the target numeric-only and not empty?")
for target in targets:
    print(f"'{target}':", target.isdigit())
print()

print("Is the target alpha-numeric-only and not empty?")
for target in targets:
    print(f"'{target}':", target.isalnum())
print()
