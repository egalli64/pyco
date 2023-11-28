"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 3 - Dictionary

Definition
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

try:
    print(users[3])
except KeyError:
    print("Can't access a value for a missing key!")
