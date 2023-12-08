"""
Python Course

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Arithmetic operators on integer and float
"""
x = 1
print("x is", x)

# Unary operators
y = +x
print("if y = +x, its value is", y)  # 1

y = -x
print("if y = -x, its value is", y)  # -1

print("---")
a = 10
b = 3
c = 3.0
print(f"a is {a}, b is {b}, c is {c}")

# Arithmetic operators
print(f"{a} + {b} =", a + b)  # 13
print(f"{a} + {c} =", a + c)  # 13.0

print(f"{a} - {b} =", a - b)  # 7
print(f"{a} * {b} =", a * b)  # 30
print(f"{a} ** {b} =", a ** b)  # 1000

print(f"{a} / {b} =", a / b)  # 3.3333333333333335
print(f"{a} / {c} =", a / c)  # 3.3333333333333335

print(f"{a} // {b} =", a // b)  # 3
print(f"{a} // {c} =", a // c)  # 3.0

print(f"{a} % {b} =", a % b)  # 1
print(f"{a} % {c} =", a % c)  # 1.0
print(f"-{a} % {b} =", -a % b)  # 2

# beware of floating point rounding
d = 2.1
print(f"{c} - {d} =", c - d)  # 0.8999999999999999

# beware of division by zero
try:
    z = a / 0
except ZeroDivisionError:
    print("Can't divide an integer by zero!")

try:
    z = c / 0
except ZeroDivisionError:
    print("Can't divide a float by zero!")


# Assignment and compound assignment operators
x = 2
print("x is", x)

x += 8
print("After 'x += 8', x is", x)  # 10

x -= 3
print("After 'x -= 3', x is", x)  # 7

x *= 2
print("After 'x *= 3', x is", x)  # 14

x //= 2
print("After 'x //= 2', x is", x)  # 7

x %= 5
print("After 'x %= 5', x is", x)  # 2

# The assignment expression
x = 30 + (y := 12)
print(f"Assigning values to both x ({x}) and y ({y})")
