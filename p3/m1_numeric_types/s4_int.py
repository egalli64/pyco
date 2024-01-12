"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Numeric Types

int
"""
# a large integer
x = 2**1_000
print(f"A value of type {type(x)} could be very large: {x}\n")

# non-decimal representations
print("The binary number 0b10 has decimal representation", 0b10)
print("The octal number 0o12345670 has decimal representation", 0o12345670)
print("The hexadecimal number 0x1234567890ABCDEF has decimal representation", end=" ")
print(0x1234567890ABCDEF)
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
    print(ex)
finally:
    print()

# power
print(f"{a} ** {b} is", a**b)
print(f"pow({a}, {b}) is", pow(a, b))
print()

# division and module
a = 48
print(f"{a} // {b} is", a // b)
print(f"{a} % {b} is", a % b)
print(f"divmod({a}, {b}) is", divmod(a, b))
