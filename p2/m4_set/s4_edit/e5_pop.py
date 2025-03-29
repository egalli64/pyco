"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Editing by pop()
"""

# a set
friends = {"bob", "kim", "tom"}
print("Friends:", friends)

# pop() until the set is empty
while friends:
    print(friends.pop(), "was a friend - popped!")

# can't pop on an empty set
try:
    friends.pop()
except KeyError as ex:
    print("KeyError!", ex)
