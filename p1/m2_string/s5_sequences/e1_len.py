"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequences - the built-in len()
"""

# all sequences support len()

# a string is a sequence
str = "welcome to Python's world"
print(f"The length of '{str}' is", len(str))

# a list is a sequence, too
lis = ["bob", "tom", "kim", "tim"]
print(f"The length of '{lis}' is", len(lis))

# but there are also non-sequences supporting len()

# a set is not a sequence, still it supports len()
set = {5, 4, 3, 2, 1}
print(f"The length of '{set}' is", len(set))
