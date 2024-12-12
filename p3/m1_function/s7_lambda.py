"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Lambda
"""

xs = [1, 2, 3, 4, 5]
print("The orginal values", xs)


# mapping


def to_square(x):
    """helper to map without a lambda"""
    return x**2


print("The squared values (by function)", list(map(to_square, xs)))
print("The squared values (by lambda)", list(map(lambda x: x**2, xs)))


# filtering


def is_even(x):
    """helper to filter without a lambda"""
    return x % 2 == 0


print("The even values (by function)", list(filter(is_even, xs)))
print("The even values (by lambda)", list(filter(lambda x: x % 2 == 0, xs)))


# sorting

names = ["billy", "bo", "tom"]
print("Names are:", names)


def to_len(x):
    """helper to convert a string to its lenght"""
    return len(x)


print("Names sorted by length (by function)", list(sorted(names, key=to_len)))
print("Names sorted by length (by lambda)", list(sorted(names, key=lambda x: len(x))))
