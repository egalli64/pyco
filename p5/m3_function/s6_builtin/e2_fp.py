"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Builtin - support to Functional Programming
"""

from functools import reduce

names = ("Tom", "Bob", "Joe", "Jim")
print("Names:", names)

# map
genitives = tuple(map(lambda x: x + "'s", names))
print("Genitives:", genitives)

# filter
j_names = tuple(filter(lambda x: x.startswith("J"), names))
print("Names starting with J:", j_names)

# reduce
total_len = reduce(lambda acc, x: acc + len(x), names, 0)
print("Total len of names:", total_len)
