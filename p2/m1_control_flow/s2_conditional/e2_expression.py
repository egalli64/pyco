"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - Control Flow

Conditional expression
"""

import random

# a float in [0.0 .. 1.0)
value = random.random()
print(f"Different behavior accordingly to the random value {value}\n")

# using the conditional expression
description = "low" if value < 0.5 else "high"
print(f"The value is {description}")

# same, but using a plain if - else
if value < 0.5:
    description = "close enough to zero"
else:
    description = "close enough to one"
print(f"The value is {description}")
