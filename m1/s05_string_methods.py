"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 1 - Fundamental concepts

A few string methods
"""

s = "welcome to Python"
print(f"The length of '{s}' is", len(s))

# Uppercase / Lowercase
print("Capitalized:", s.capitalize())
print("Titled:", s.title())
print("Uppercased:", s.upper())
print("Lowercased:", s.lower())

# Strip
t = "  welcome to Python!  "
print(f"A string: '{t}'")
print(f"Left strip: '{t.lstrip()}'")
print(f"Right strip: '{t.rstrip()}'")
print(f"Left/right strip: '{t.strip()}'")

# Check start/end
p = "Python"
print(f"'{s}' starts with '{p}'?", s.startswith(p))
print(f"'{s}' ends with '{p}'?", s.endswith(p))

# find a substring
j = "Java"
print(f"Find '{j}' in '{s}':", s.find(j))
print(f"Find '{p}' in '{s}':", s.find(p))

# index of the first substring
try:
    print(f"Index of '{p}' in '{s}':", s.index(p))
    print(f"Index of '{j}' in '{s}':", end=" ")
    print(s.index(j))
except ValueError:
    print("Not found!")

# count substrings
print(f"Count occurrences of '{j}' in '{s}':", s.count(j))
print(f"Count occurrences of '{p}' in '{s}':", s.count(p))
