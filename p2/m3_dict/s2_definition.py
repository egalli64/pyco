"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Definition
"""

# literal definition for a user
alice = {"name": "Alice", "age": 32, "city": "Madrid"}
print("A user:", alice)

# constructor for a user
bob = dict(name="Bob", age=42, city="Berlin")
print("Another user:", bob)

# literal definition of a dictionary representing more users
users = {27: alice, 42: bob}
print("A dictionary of users:", users)

# dictionary comprehension
odd_squared = {x: x**2 for x in range(1, 11) if x % 2 != 0}
print("A dictionary of odd numbers and their squared values:", odd_squared)
