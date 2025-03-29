"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Editing by add()
"""

# a set
friends = {"bob", "kim", "tom"}
print("Friends:", friends)

# add an element
new_friend = "mia"
friends.add(new_friend)
print(f"After adding '{new_friend}':", friends)

# no effect - duplicate is silently discarded
friends.add(new_friend)
print(f"After trying to add '{new_friend}' a second time:", friends)
