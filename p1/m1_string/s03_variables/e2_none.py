"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Strings and variables

Variables - None
"""
# no "actual" value associated to x
x = None

print("The value of x is", x)
print("Type of x is", type(x))

# preferred way to check against None
if x is None:
    print("The object referenced by x is None")

# this works too, but checking the id is more robust and clean
# if x == None:
#    print("The comparison of x against None succeed")

y = None
if x == y and x is y:
    print("None is None, in every possible way")
