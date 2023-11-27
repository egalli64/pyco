"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 2 - Control Flow

Branching
"""

s = "Welcome To Pythonville"

# stop printing if a blank is found
for c in s:
    if c == ' ':
        break
    else:
        print(c, end="")
print()

# skip blanks
for c in s:
    if c == ' ':
        continue
    else:
        print(c, end="")
print()

# skip blanks, without using continue
for c in s:
    if c != ' ':
        print(c, end="")
print()


def print_first_word(s):
    """A function that prints up to the first blank"""
    for c in s:
        if c == ' ':
            return
        else:
            print(c, end="")


print_first_word(s)
print()
