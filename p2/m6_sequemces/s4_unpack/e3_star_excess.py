"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 6 - Sequence

Unpacking
The * operator for values in excess
"""
point = (53, 12)
print("my point is", point)

# star on args
div, mod = divmod(*point)
print(f"{point[0]} // {point[1]} =", div)
print(f"{point[0]} % {point[1]} =", mod)

# star to capture more values
values = list(range(5))
print("values are", values)
a, b, *rest = values
print("the values in excess are", rest)
a, *rest, b = values
print("now the values in excess are", rest)
*rest, a, b = values
print("now the values in excess are", rest)
a, b, *rest = point
print("the values in excess are", rest)


# packing arguments in excess in the last parameter
def f(a, b, *c):
    print("function f():", a, b, c)


# unpacking the arguments, the last ones will be packed in the last parameter
f(*values)
