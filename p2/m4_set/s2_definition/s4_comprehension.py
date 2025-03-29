"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 4 - Set

Definition - comprehension
"""

values = {x for x in range(20, 30, 3)}
print("A set from comprehension:", values)

values = {x**2 for x in range(10) if x % 2 == 0}
print("Another set from comprehension:", values)
