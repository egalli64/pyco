"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 2 - List

Tuple
"""

# a tuple
friends = ("bob", "tom", "kim", "abe", "luc")
print(f"friends in a tuple: {friends}\n")

print("The first friend is", friends[0])

# mutable functionality are not available
print("Can't change elements in a tuple:", end=" ")
try:
    friends[0] = "bill"
except TypeError:
    print("Tuples are immutable!")

# a single-element tuple, parenthesis are not mandatory here!
best_friend = ("joe",)
print("A tuple with a single element:", best_friend)

# assign a new tuple
best_friend = ("tim",)
print("tuples are immutable, but a variable can be reassigned:", best_friend)

# tuple comprehension
squared_evens = tuple(x**2 for x in range(10) if x % 2 == 0)
print("Not really a comprehension, but close enough:", squared_evens)
