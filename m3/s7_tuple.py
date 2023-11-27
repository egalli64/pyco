"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 3 - List

Tuple
"""
# a tuple
friends = ("bob", "tom", "kim", "abe", "luc")
print("friends:", friends)

print("The first friend is", friends[0])

try:
    friends[0] = "bill"
except TypeError:
    print("Tuples are immutable!")

# a single-element tuple
best_friend = ("joe",)
print(best_friend)

# assign a new tuple
best_friend = ("tim", )
print(best_friend)

# tuple comprehension
squared_evens = tuple(x**2 for x in range(10) if x % 2 == 0)
print(squared_evens)
