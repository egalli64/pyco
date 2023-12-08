"""
Python Course

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Operator precedence and association
"""

# by default, multiply first
print(2 + 6 * 7 - 3)      # 41

# rearrange in the preferred way
print((2 + 6) * (7 - 3))  # 32

# TODO: use parentheses to fix the bug
x = 1.0
result = 1 / x + 1 / x + 1 / x + 1 / x
print("Actual result is:", result)
print("Expected result is: 0.6000000000000001")
