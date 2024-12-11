"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 4 - Control Flow

Conditional statements
"""
import random

# a float in [0.0 .. 1.0)
value = random.random()
print(f"Executing different statements accordingly to the random value {value}\n")

print("* 1. check if value is bigger than 0.5")

# do nothing if condition is False
if value > 0.5:
    print("Close enough to 1")

print("* 2. check if in (0.25 .. 0.75), or else")

# one choice or the other
print("The value", end=" ")
if value > 0.25 and value < 0.75:
    print("is close enough to 0.5")
else:
    print("is too far away from 0.5")

print("* 3. check if less then 1/3, elif less then 2/3, or else")

# one of the three block will be executed
if value < 0.33:
    print("Close enough to 0.0:")
elif value < 0.66:
    print("Close enough to 0.5:")
else:
    print("Close enough to 1.0:")

# using 'pass' as placeholder
print("* 4. check if less than 1/2, else pass")
if value < 0.5:
    print("Small value")
else:
    # should do something, but currently I don't know what
    pass
