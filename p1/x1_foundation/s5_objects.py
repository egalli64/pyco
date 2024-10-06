"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Foundation

Objects
"""

# defining a few variables
message = "Hello!"
flag = True
answer = 42
price = 12.21

# the type of a variable is the type of the object it currently references
print("Type of message is", type(message))
print("Type of flag is", type(flag))
print("Type of answer is", type(answer))
print("Type of price is", type(price))

# check if the type is the expected one by isinstance
print("Is message a str?", isinstance(message, str))
print("Is message an int?", isinstance(message, int))
print("Is answer a float or an int?", isinstance(answer, (float, int)))
print("Is answer a str?", isinstance(answer, str))

# the unique id associated with the referenced objects
print("message id:", id(message))
print("flag id:", id(flag))
