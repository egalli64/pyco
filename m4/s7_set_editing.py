"""
Python Course

https://github.com/egalli64/pyco

Module 4 - Dictionary and set

Set: add, remove, ...
"""
# a set
friends = {"bob", "tom", "kim"}
print("Friends:", friends)

# add an element
friends.add("mia")
friends.add("mia")
print("Friends (add):", friends)

# update a set with an iterable
others = ["tom", "zoe"]
friends.update(others)
print("Friends (update):", friends)

# remove an element
try:
    friends.remove("tom")
    print("Friends (remove):", friends)
    friends.remove("tom")
except KeyError as ex:
    print("Can't remove a missing element:", ex)

# discard an element
friends.discard("kim")
friends.discard("kim")
print("Friends (discard):", friends)

# pop an element
while len(friends):
    cur = friends.pop()
    print(cur, "was a friend (pop)")
print("Friends (pop):", friends)

try:
    friends.pop()
except KeyError as ex:
    print("KeyError!", ex)
