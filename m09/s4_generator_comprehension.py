"""
Python Course

https://github.com/egalli64/pyco

Module 9 - More on functions

Generator comprehension
"""

# Generator comprehension for the first even squared values
for cur in (n**2 for n in range(10) if n % 2 == 0):
    print(cur, end=" ")
print()


def even_squared(begin=0, end=10):
    """More flexible, by generator function"""
    current = begin if begin % 2 == 0 else begin + 1
    for n in range(current, end, 2):
        yield n**2


# Iterate on the generator
for cur in even_squared():
    print(cur, end=" ")
print()

for cur in even_squared(-3, 8):
    print(cur, end=" ")
print()


class EvenSquaredIterator:
    """More flexible, by iterator"""

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
for cur in EvenSquaredIterator():
    print(cur, end=" ")
print()

for cur in EvenSquaredIterator(-3, 8):
    print(cur, end=" ")
print()
