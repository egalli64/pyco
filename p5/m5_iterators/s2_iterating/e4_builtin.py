"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Iterable and iterator

Iterating with built-in functions iter() and next()
"""

from e3_modern_iter import IterableInt

digits = IterableInt(347_123_348_922)
print(digits)

# get an iterator on the IntDigits iterable
it = iter(digits)

while True:
    try:
        # get the next element of the iterable through the iterator
        digit = next(it)
        print(digit, end=" ")
    except StopIteration:
        # no more elements in the iterable
        print()
        break
