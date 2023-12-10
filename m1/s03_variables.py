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
print("message:", message)
print("unknown", unknown)
print("ANSWER:", ANSWER)

# using an undefined variable is a NameError
# print(mesage)

# the type of a variable is the type of the object it currently references
print("Type of message is", type(message))
print("Type of unknown is", type(unknown))
print("Type of ANSWER is", type(ANSWER))

# check if the type is the expected one by isinstance
print("Is message a str?", isinstance(message, str))
print("Is message an int?", isinstance(message, int))
print("Is ANSWER a float or an int?", isinstance(ANSWER, (float, int)))
print("Is ANSWER a str?", isinstance(ANSWER, str))

# the unique id associated with the referenced objects
print("message id:", id(message))
print("unknown id:", id(unknown))
print("ANSWER id:", id(ANSWER))
