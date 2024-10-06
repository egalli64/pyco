"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - Numbers and operators

Numeric types
Real numbers: float
"""
f = 123_456.789e18
print("f is", f, type(f))

print("to bool:", bool(f))
print("to int:", int(f))

# bool to float
f = float(True)
print("True as float:", f)

# int to float
f = float(42)
print("42 as float:", f)
