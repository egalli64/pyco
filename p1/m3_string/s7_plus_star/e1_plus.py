"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Strings and variables

Sequence concatenation
"""
a = "alpha"
b = "beta"
print(f"a is {a}, b is {b}\n")

# assign to s the concatenation of a and b
s = a + b
print(f"{a} + {b} =", s)

# assign to s the concatenation of s and b
print(f"{s} += {b} =", end=" ")
s += b
print(s, "\n")

# assign to message the concatenation of first, second, and third string to right
message = "Resistence" + " is " + "useless"
print(message, "\n")

try:
    # can't concatenate string and non-string
    message = "it is not " + 2 + " late"
except TypeError:
    print("Concatenation works only on strings!\n")

# same as: message = message + "!"
message += "!"
print(message)
