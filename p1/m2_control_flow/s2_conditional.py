"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - Control Flow

Conditional statements and conditional expression
"""
import random

# a float in [0.0 .. 1.0)
value = random.random()

# conditional statements
print("First step")

# do nothing if condition is False
if value > 0.5:
    print("Close enough to 1")

print("Second step")

# one choice or the other
if value > 0.25 and value < 0.75:
    print("Close enough to 0.5")
else:
    print("Too far away from 0.5")

print("Third step")

# one of the three block will be executed
if value < 0.33:
    print("Close enough to 0.0:", value)
elif value < 0.66:
    print("Close enough to 0.5:", value)
else:
    print("Close enough to 1.0:", value)

# conditional expression
description = "low" if value < 0.5 else "high"
print("The value is", description)

# using 'pass' as placeholder
if value < 0.5:
    print("Small value")
else:
    # should do something, but currently I don't know what
    pass
