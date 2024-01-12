"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Numeric Types

int
"""
# non-decimal representations
print("the binary number 0b10 has decimal representation", 0b10)
print("the octal number 0o12345670 has decimal representation", 0o12345670)
print("the hexadecimal number 0x1234567890ABCDEF has decimal representation", end=" ")
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
