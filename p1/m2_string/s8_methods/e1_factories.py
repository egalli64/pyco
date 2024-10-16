"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

String modifier factories
"""
# A string
s = "welcome to Python's world"

# Uppercase / Lowercase
print("Capitalized:", s.capitalize())
print("Titled:", s.title())
print("Uppercased:", s.upper())
print("Lowercased:", s.lower())
print()

# Strip
t = "  welcome to python!  "
print(f"A string: '{t}'")
print(f"Left strip: '{t.lstrip()}'")
print(f"Right strip: '{t.rstrip()}'")
print(f"Left/right strip: '{t.strip()}'")
print()

# Replace
print("Replacing Python:", s.replace("Python", "Programming"))
print("Replacing 'o's:", s.replace("o", "_"))
