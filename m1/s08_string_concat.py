"""
Python Course

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

String concatenation and repetition
"""

message = "Resistence" + " is " + "useless"
print(message)

try:
    message = "it is not " + 2 + " late"
except TypeError:
    print("Concatenation works only on strings!")

# same as: message = message + "!"
message += "!"
print(message)

message_2 = "hello " * 3
print(message_2)

try:
    message_2 = 3.4 * "hello "
except TypeError:
    print("Repetition works only on one string and one integer!")

# same as: message_2 = message_2 * 3
message_2 *= 2
print(message_2)
