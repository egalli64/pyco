"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Editing by remove()
"""

# a set
friends = {"bob", "kim", "tom"}
print("Friends:", friends)

# if it is in the friend set, it should be removed
no_friend = "tom"

# check if it is in the set before removing it
if no_friend in friends:
    friends.remove(no_friend)
    print(f"After removing '{no_friend}':", friends)

# remove it, or throw a KeyError
try:
    print(f"Trying to remove '{no_friend}' ...")
    friends.remove(no_friend)
except KeyError as e:
    print("Can't remove it if it is missing:", e)
