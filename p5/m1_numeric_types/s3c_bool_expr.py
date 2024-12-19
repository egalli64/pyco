"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 1 - Numeric Types

Conditional Expressions
"""

a = 0
b = 3
c = 10

print(f"a is {a}, b is {b}, c is {c}")

# 1. explicit, more readable
if a:
    result = a
else:
    result = b
print("result = 'a' if 'a' is truthy, otherwise is 'b':", result)

# 2. conditional expression by if - else, compact and flexible
result = a if a else b
print("same (conditional expression by if - else):", result)

# 3. conditional expression by or, very compact
result = a or b
print("same (conditional expression by or):", result)

# 4. conditional expression by and
result = b and c
print("result = 'b' if 'b' is falsy, otherwise is 'c':", result)
