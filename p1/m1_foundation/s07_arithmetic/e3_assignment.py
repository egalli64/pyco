"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Arithmetic operators - assignments and compound assignments
"""
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
