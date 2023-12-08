"""
Python Course

https://github.com/egalli64/pyco

Module 4 - Dictionary and set

Dictionary
"""
# a dictionary representing a user
alice = {"name": "Alice", "age": 32, "city": "Madrid"}
print(alice)
print("Alice age is", alice["age"])

# another dictionary for another user
bob = dict(name="Bob", age=42, city="Berlin")
print(bob)
print("Bob city is", bob["city"])

# a dictionary representing more users
users = {1: alice, 2: bob}
print(users)
print("User 1 is", users[1])

# dictionary comprehension
even_squared = {x: x**2 for x in range(1, 11) if x % 2 != 0}
print(even_squared)

# be careful when using a key to access a value
try:
    print(users[3])
except KeyError:
    print("Can't access a value for a missing key!")

# get() by default return None when the key is missing
print(users.get(3))
print(users.get(3, "Can't find the passed key!"))
