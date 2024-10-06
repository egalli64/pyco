"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 4 - Sequence

Iterable and iterator
A non iterable class
"""


class NotIterableDigits:
    """Not implementing __getitem__ nor __iter__ this class is not iterable"""

    def __init__(self, value):
        self._value = value
        self._buffer = str(value)

    def __repr__(self):
        return f"NotIterableDigits({self._value})"


digits = NotIterableDigits(347_123_348_922)
print(digits)

try:
    # not iterable
    iter(NotIterableDigits(42))
except TypeError as ex:
    print(ex)
