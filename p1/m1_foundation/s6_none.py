"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Foundation

Variables - None
"""

# assign an int object to x
x = 42
print("The value of x is", x, end=", ")
print("and its type is", type(x))

# no "actual" value associated to x
x = None

print("Now the value of x is", x, end=", ")
print("and its type is", type(x))

# in a boolean context, None is considered False
if not x:
    print("The object referenced by x is falsy (it could be None)")


# preferred way to check against None
if x is None:
    print("The object referenced by x is None")

# this works too, but checking the id is more robust, clean, and efficient
if x == None:
    print("The equality comparison of x against None succeed")

y = None
if x == y and x is y:
    print("None is None, in every possible way")
