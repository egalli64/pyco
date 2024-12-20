"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Check - start/end
"""

s = "Welcome to Python"
targets = ("Welcome", "Python")

print(f"Is '{s}' starting for ...")
for target in targets:
    print(f"'{target}':", s.startswith(target))
print()

print(f"Is '{s}' ending for ...")
for target in targets:
    print(f"'{target}':", s.endswith(target))
print()
