"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 2 - More on functions

Generator comprehension
"""


def even_squared(begin=0, end=10):
    """A generator function, returning the square of even values in [begin .. end)"""
    current = begin if begin % 2 == 0 else begin + 1
    for n in range(current, end, 2):
        yield n**2


# Iterate on the generator
print("Even squared in [0 .. 10):", end=" ")
for cur in even_squared():
    print(cur, end=" ")
print()

# Using another generator on a different interval
print("Even squared in [-3 .. 8):", end=" ")
for cur in even_squared(-3, 8):
    print(cur, end=" ")
print()


# Generator comprehension, more compact
print("Even squared in [0 .. 10) by comprehension:", end=" ")
for cur in (n**2 for n in range(10) if n % 2 == 0):
    print(cur, end=" ")
print()


class EvenSquaredIterator:
    """More flexible, same functionality by iterator"""

    def __init__(self, begin=0, end=10):
        self.current = begin if begin % 2 == 0 else begin + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current**2
            self.current += 2
            return result
        else:
            raise StopIteration


# Using the iterator
print("Even squared in [0 .. 10) by iterator:", end=" ")
for cur in EvenSquaredIterator():
    print(cur, end=" ")
print()

print("Even squared in [-3 .. 8) by iterator:", end=" ")
for cur in EvenSquaredIterator(-3, 8):
    print(cur, end=" ")
print()
