"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Definition - constructor
"""

# a set generated from a list
info = [1, 2, 2, 2]
unique_info = set(info)
print(f"From list {info} to set {unique_info}")

# a set generated from a string
name = "emanuele"
letters = set(name)
print(f"From string '{name}' to set {letters}")
