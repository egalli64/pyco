"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 3 - Control Flow

Conditional expression
"""
import random

# a float in [0.0 .. 1.0)
value = random.random()
print(f"Different behavior accordingly to the random value {value}\n")

description = "low" if value < 0.5 else "high"
print(f"The value is {description}")
