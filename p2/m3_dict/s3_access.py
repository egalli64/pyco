"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - Dictionary

Access
"""

# a dictionary
even_squared = {x: x**2 for x in range(1, 11) if x % 2 != 0}
print("Working on this dictionary:", even_squared)

# using the in operator
if 7 in even_squared:
    print("7 is in it")

# using not in
if 10 not in even_squared:
    print("10 is not in it")

# checking if a dictionary is not empty
if even_squared:
    print("The dictionary is not empty")

if not {}:
    print("An empty dictionary is False in boolean context")

# access a value by square brackets
print("The value associated to 7 is:", even_squared[7])

# be careful when using a key to access a value by square brackets
try:
    print(even_squared[10])
except KeyError as ex:
    print("Can't access a value for missing key:", ex)

# or, use the in check before accessing it
if 10 in even_squared:
    print(even_squared[10])
else:
    print("Can't access a value for a missing key")

# get() by default return None when the key is missing
value = even_squared.get(10)
print("Get value for key 10 (missing):", value)

# the get() default return value can be given by the caller
value = even_squared.get(10, "Can't find the passed key!")
print("Get value for key 10 (default):", value)