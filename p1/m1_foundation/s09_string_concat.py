"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

String concatenation and repetition
"""
a = "alpha"
b = "beta"

# assign to s the concatenation of a and b
s = a + b
print(s)

# assign to s the concatenation of s and b
s += b
print(s)

# assign to message the concatenation of first, second, and third string to right
message = "Resistence" + " is " + "useless"
print(message)

try:
    # can't concatenate string and non-string
    message = "it is not " + 2 + " late"
except TypeError:
    print("Concatenation works only on strings!")

# same as: message = message + "!"
message += "!"
print(message)

# assign to rhs the "multiplication" of the rhs string by 3
message_2 = "hello " * 3
print(message_2)

try:
    # can't multiply string and non-int
    message_2 = 3.4 * "hello "
except TypeError:
    print("Repetition works only on one string and one integer!")

# same as: message_2 = message_2 * 3
message_2 *= 2
print(message_2)
