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


# step 1: map() returns an iterator that would generate the mapped iterable
iter = map(to_square, xs)
# step 2: generate the required mapped iterable, here a list
ls = list(iter)
# step 3: use it
print("The squared values (by function)", ls)
# same as:
print("The squared values (by function)", list(map(to_square, xs)))

print("The squared values (by lambda)", list(map(lambda x: x**2, xs)))

# map a matrix to a list
matrix = [(1, 3), (2,), (4, 4, 1)]
mapped = list(map(sum, matrix))  # -> [4, 2, 9]
print(f"{matrix} mapped to {mapped}")


# filtering


def is_even(x):
    """helper to filter without a lambda"""
    return x % 2 == 0


print("The even values (by function)", list(filter(is_even, xs)))
print("The even values (by lambda)", list(filter(lambda x: x % 2 == 0, xs)))


# sorting


names = ["tom", "billy", "bo"]
print("Names are:", names)

xs = sorted(names)
print("Sorted (natural):", xs)


def to_len(x):
    """helper to convert a string to its lenght"""
    return len(x)


print("Names sorted by length (by function)", sorted(names, key=to_len))
print("Names sorted by reversed length (by function)", sorted(names, key=to_len, reverse=True))
print("Names sorted by length (by lambda)", sorted(names, key=lambda x: len(x)))
print("Names sorted by length (by built-in)", sorted(names, key=len))
