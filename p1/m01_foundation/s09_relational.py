"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Relational operators
"""

alpha = 12
beta = 21
gamma = 12
print(f"alpha is {alpha}, beta is {beta}, gamma is {gamma}")

result = alpha < beta  # True
print("alpha < beta?", result)

result = alpha < gamma  # False
print("alpha < gamma?", result)

result = alpha <= gamma  # True
print("alpha <= gamma?", result)

result = alpha > beta  # False
print("alpha > beta?", result)

result = alpha > gamma  # False
print("alpha > gamma?", result)

result = alpha >= gamma  # True
print("alpha >= gamma?", result)

result = alpha == beta  # False
print("alpha == beta?", result)

result = alpha == gamma  # True
print("alpha == gamma?", result)

result = alpha != beta  # True
print("alpha != beta?", result)

result = alpha != gamma  # False
print("alpha != gamma?", result)

f_alpha = 12.0
print("alpha == f_alpha?", alpha == f_alpha)
