"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Numeric types
Boolean: bool
"""
flag = False
print("flag is", flag, type(flag))

flag = True
print("now flag is", flag)

print("True is 1, in numeric context:", 42 * True)
print("False is 0:", 42 * False)

print("Casted to boolean, each non-zero number is True:", bool(42) == True)
print("Casted to boolean, zero is False:", bool(0.0) == False)
