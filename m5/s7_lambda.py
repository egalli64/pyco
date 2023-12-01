"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 5 - Function

Lambda
"""
xs = [1, 2, 3, 4, 5]
print("The orginal values", xs)

# mapping


def to_square(x):
    """helper to map without a lambda"""
    return x**2


squared = list(map(to_square, xs))
print("The squared values (by function)", squared)

squared = list(map(lambda x: x**2, xs))
print("The squared values (by lambda)", squared)

# filtering


def is_even(x):
    """helper to filter without a lambda"""
    return x % 2 == 0


even = list(filter(is_even, xs))
print("The even values (by function)", even)


even = list(filter(lambda x: x % 2 == 0, xs))
print("The even values (by lambda)", even)
