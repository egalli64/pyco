"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 3 - Control Flow

Conditional statements
"""
import random

# a float in [0.0 .. 1.0)
value = random.random()
print(f"Executing different statements accordingly to the random value {value}\n")

print("* First step (if)")

# do nothing if condition is False
if value > 0.5:
    print("Close enough to 1")

print("* Second step (if - else)")

# one choice or the other
print("The value", end=" ")
if value > 0.25 and value < 0.75:
    print("is close enough to 0.5")
else:
    print("is too far away from 0.5")

print("* Third step (if - elif - else)")

# one of the three block will be executed
if value < 0.33:
    print("Close enough to 0.0:", value)
elif value < 0.66:
    print("Close enough to 0.5:", value)
else:
    print("Close enough to 1.0:", value)
print()

# using 'pass' as placeholder
if value < 0.5:
    print("Small value")
else:
    # should do something, but currently I don't know what
    pass
