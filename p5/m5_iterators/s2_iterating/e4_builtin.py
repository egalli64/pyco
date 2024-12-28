"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 4 - Sequence

Iterable and iterator
Use by built-in
"""
from e3_iter import IntDigits

digits = IntDigits(347_123_348_922)
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
