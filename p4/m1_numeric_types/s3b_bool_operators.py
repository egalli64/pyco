"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - Numeric Types

bool operators
"""
a = True
b = False

print("AND truth table")
for a in False, True:
    for b in False, True:
        print(f"{a} and {b} is", a and b)
print()

print("OR truth table")
for a in False, True:
    for b in False, True:
        print(f"{a} or {b} is", a or b)
print()

print("NOT truth table")
for a in False, True:
    print(f"not {a} is", not a)
print()

print("XOR truth table")
for a in False, True:
    for b in False, True:
        print(f"{a} != {b} is", a != b)
print()

print("Using bitwise operator (meh)")
print("AND truth table")
for a in False, True:
    for b in False, True:
        print(f"{a} & {b} is", a & b)
print()

print("OR truth table")
for a in False, True:
    for b in False, True:
        print(f"{a} | {b} is", a | b)
print()

print("XOR truth table")
for a in False, True:
    for b in False, True:
        print(f"{a} ^ {b} is", a ^ b)
print()
