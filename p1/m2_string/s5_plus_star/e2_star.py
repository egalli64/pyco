"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

Sequence repetition
"""
# assign to message the "multiplication" of the hello string by 3
message = "hello " * 3
print(message)

try:
    # can't multiply string and non-int
    message = 3.4 * "hello "
except TypeError:
    print("Repetition works only on one string and one integer!")

# same as: message = message * 2
message *= 2
print(message)
