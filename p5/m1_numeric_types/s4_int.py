"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 1 - Numeric Types

int
"""

# a large integer
x = 2**1_000
print(f"A value of type {type(x)} could be very large: {x}\n")

# non-decimal representations
x = 0b10
print(f"The binary number {x:#b} has decimal representation", x)

x = 0o12345670
print(f"The octal number {x:#o} has decimal representation", x)

x = 0x1234567890ABCDEF
print(f"The hexadecimal number {x:#x} has decimal representation", x)
print()

# int vs float division
a = 6
b = 3
x = a / b
print(f"{a} / {b} is {x}, a float:", isinstance(x, float))
x = a // b
print(f"{a} // {b} is {x}, an int:", isinstance(x, int))

b = 5
x = a / b
print(f"{a} / {b} is {x}, a float:", isinstance(x, float))
x = a // b
print(f"{a} // {b} is {x}, an int:", isinstance(x, int))
print()

# division by zero
try:
    print(a / 0)
except ZeroDivisionError as ex:
    print("ZeroDivisionError:", ex)
finally:
    print()

# modulo
a = 48
print(f"{a} % {b} is", a % b)
print(f"{-a} % {b} is", -a % b)

# modulo by zero
try:
    print(a % 0)
except ZeroDivisionError as ex:
    print("ZeroDivisionError:", ex)
finally:
    print()
