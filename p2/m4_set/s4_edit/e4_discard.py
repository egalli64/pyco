"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Editing by discard()
"""

# a set
friends = {"bob", "kim", "tom"}
print("Friends:", friends)

# if it is in the friend set, it should be removed
no_friend = "tom"

# discard it, or ignore the request
friends.discard(no_friend)
print(f"After discarding '{no_friend}':", friends)

print(f"Trying to discard '{no_friend}' a second time ...")
friends.discard(no_friend)
print(f"After non-discarding '{no_friend}':", friends)
