"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - Numbers and operators

Logical operators
"""
alpha = True
beta = False
print(f"alpha is {alpha}, beta is {beta}")

truthy = "Hello"
falsy = 0
print(f"truthy is {truthy}, falsy is {falsy}")

# and
result = beta and alpha    # False
print("beta and alpha?", result)

result = truthy and falsy  # falsy, here 0
print("truthy and falsy?", result)

# or
result = alpha or beta     # True
print("alpha or beta?", result)

result = truthy or falsy   # truthy, here 'Hello'
print("truthy or falsy?", result)

# not
print("not alpha?", not alpha)  # False
print("not falsy?", not falsy)  # True
