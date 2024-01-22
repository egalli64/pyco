"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - Numbers and operators

Assignments - statement and expression
"""
# The assignment statement
a = 2
b = 3

x = a
print("x is", a)

# The simple assignment of a value to more variables works fine
x = y = b
print(f"Assigning a value to x ({x}) and y ({y})")

# But assigning a value to a variable and use it in an expression does not work
# x = 30 + (y = 12)

# The assignment expression allows it
x = b + (y := a)
print(f"Assigning values to x ({x}) and y ({y})")

# The walrus used as a statement won't compile, it requires parentheses
# x := a

# Ugly and useless
(x := a)
print("x is", a)
