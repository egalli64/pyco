"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - Numbers and operators

Arithmetic operators
"""
a = 10
b = 3
c = 3.0
print(f"a is {a}, b is {b}, c is {c}\n")

# +
print(f"{a} + {b} =", a + b)  # 13
print(f"{a} + {c} =", a + c)  # 13.0

# -
print(f"{a} - {b} =", a - b)  # 7
print(f"{a} - {c} =", a - c)  # 7.0
print()

# *
print(f"{a} * {b} =", a * b)  # 30
print(f"{a} * {c} =", a * c)  # 30.0

# **
print(f"{a} ** {b} =", a**b)  # 1000
print(f"{a} ** {c} =", a**c)  # 1000.0
print()

# /
print(f"{a} / {b} =", a / b)  # 3.3333333333333335
print(f"{a} / {c} =", a / c)  # 3.3333333333333335

# //
print(f"{a} // {b} =", a // b)  # 3
print(f"{a} // {c} =", a // c)  # 3.0
print()

print(f"{a} % {b} =", a % b)  # 1
print(f"{a} % {c} =", a % c)  # 1.0
print(f"-{a} % {b} =", -a % b)  # 2
print(f"-{a} % {c} =", -a % c)  # 2.0
print()

# beware of floating point rounding: 3.0 - 2.1 is ...
d = 2.1
print(f"{c} - {d} =", c - d)  # 0.8999999999999999
print()

# beware of division by zero
try:
    z = a / 0
except ZeroDivisionError:
    print("Can't divide an integer by zero!")

try:
    z = c / 0
except ZeroDivisionError:
    print("Can't divide a float by zero!")
