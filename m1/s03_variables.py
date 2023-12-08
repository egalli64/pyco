"""
Python Course

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Variables
"""

# defining a few variables
message = "Hello!"
unknown = None
# please, consider this variable as if it was a constant
ANSWER = 42

# using previously defined variables
print(message)
print(ANSWER)
print(unknown)

# using an undefined variable is a (Name) error
# print(mesage)

# the type of a variable is the type of the object it currently references
print(type(message))
print(type(ANSWER))
print(type(unknown))

# the unique id associated with the referenced objects
print(id(message))
print(id(ANSWER))
print(id(unknown))
