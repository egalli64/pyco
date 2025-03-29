"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Editing by clear()
"""

# a set
friends = {"bob", "kim", "tom"}
print("Friends:", friends)

friends.clear()

if not friends:
    print("After clearing, no more friends")
else:
    print("Unexpected")
