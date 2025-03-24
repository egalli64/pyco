"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - List

Inserting elements by append(), extends(), +=, insert()
"""

friends = ["bob", "tom", "kim", "abe", "luc"]
print("A list:", friends)

# append a new element (at the end)
friends.append("joe")
print("After append:", friends)

# extend with an iterable
new_friends = ("ada", "ben", "cho")
friends.extend(new_friends)
print("After extend:", friends)

# augmented concatenated assignment works alright
friends += ("dean", "emma", "fin")
# same as xs = xs + ys, but notice that with + works only between the same type
# friends = friends + ["dean", "emma", "fin"]
print("After concatenation:", friends)

# insert in the given position
friends.insert(3, "lee")
print("After insert at 3:", friends)
