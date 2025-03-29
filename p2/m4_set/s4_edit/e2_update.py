"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Editing by update()
"""

# a set
friends = {"bob", "kim", "tom"}
print("Friends:", friends)

# update a set with an iterable, tom is not inserted being already in
new_friends = ["tom", "zoe"]
friends.update(new_friends)
print(f"After updating with '{new_friends}':", friends)
