"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Definition
"""

# a literal set
friends = {"bob", "tom", "kim"}
print("A literal set:", friends)

# an empty _dictionary_
dict = {}
print("This is _not_ a set:", dict, type(dict))

# an empty set by constructor
enemies = set()
print("An empty set by constructor:", enemies, type(enemies))

# a set by constructor, getting as input an iterable of seven strings, with one duplicated "e"
letters = set("emanuele")
print("A set from an iterable:", letters)

# an immutable set
people = frozenset(["jo", "bo", "mo", "bo"])
print("An immutable set from an iterable:", people)

# set comprehension

values = {x for x in range(20) if x % 3 == 1}
print("A set from comprehension:", values)
