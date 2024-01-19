"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

A few string methods
"""
# The target string
s = "welcome to Python"
print(f"The length of '{s}' is", len(s))

# boolean check on start/end
p = "Python"
print(f"'{s}' starts with '{p}'?", s.startswith(p))
print(f"'{s}' ends with '{p}'?", s.endswith(p))

# find: index of a substring (or -1)
j = "Java"
print(f"Find '{j}' in '{s}':", s.find(j))
print(f"Find '{p}' in '{s}':", s.find(p))

# index: for the first substring (or exception)
try:
    print(f"Index of '{p}' in '{s}':", s.index(p))
    print(f"Index of '{j}' in '{s}':", end=" ")
    print(s.index(j))
except ValueError:
    print("Not found!")

# count substrings
print(f"Count occurrences of '{j}' in '{s}':", s.count(j))
print(f"Count occurrences of '{p}' in '{s}':", s.count(p))
