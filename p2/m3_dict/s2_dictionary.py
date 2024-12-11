"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Dictionary
"""
# a dictionary representing a user
alice = {"name": "Alice", "age": 32, "city": "Madrid"}
print("A dictionary:", alice)


def print_user(user):
    """
    A function printing the passed user

    Parameter:
    - user: a dictionary having as keys: name, age, city
    """
    print(f"{user['name']} has age {user['age']}, and lives in {user['city']}")


# another dictionary for another user
bob = dict(name="Bob", age=42, city="Berlin")
print(bob)

# calling the function that ask a user dictionary as argument
print_user(alice)
print_user(bob)

# a dictionary representing more users
users = {27: alice, 42: bob}
print("User 27 is:", users[27])

# dictionary comprehension
even_squared = {x: x**2 for x in range(1, 11) if x % 2 != 0}
print(even_squared)

# be careful when using a key to access a value
try:
    print(users[3])
except KeyError as ex:
    print("Can't access a value for missing key:", ex)

# get() by default return None when the key is missing
print("Get user 3 (missing):", users.get(3))
print("Get user 3 (missing with default):", users.get(3, "Can't find the passed key!"))
