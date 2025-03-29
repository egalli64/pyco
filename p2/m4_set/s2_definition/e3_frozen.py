"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Definition - forzenset
"""

# a sets
key_1 = {"jo", 42}

try:
    # a set is not a valid key
    a_dict = {key_1: "alpha"}
except TypeError as e:
    print("Can't use a set as a key in a dictionary,", e)

# create a frozen set from a plain set
key_2 = frozenset(key_1)
a_dict = {key_2: "beta"}
print("A dictionary:", a_dict)

try:
    bad = frozenset([["bob"], 42])
except TypeError as e:
    print("Can't put a mutable in a frozenset,", e)

key_3 = frozenset([("bob",), 42])
a_dict[key_3] = "gamma"
print("A dictionary:", a_dict)
