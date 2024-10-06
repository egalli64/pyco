"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Search in string
"""
# The target string
s = "welcome to Python"

# boolean check on start/end
p = "Python"
print(f"'{s}' starts with '{p}'?", s.startswith(p))
print(f"'{s}' ends with '{p}'?", s.endswith(p))

# find: index of a substring (or -1)
j = "Java"
print(f"Find '{j}' in '{s}':", s.find(j))
print(f"Find '{p}' in '{s}':", s.find(p))

# count substrings
print(f"Count occurrences of '{j}' in '{s}':", s.count(j))
print(f"Count occurrences of '{p}' in '{s}':", s.count(p))
print(f"Count occurrences of 'o' in '{s}':", s.count("o"))
