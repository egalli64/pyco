"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Iterable and iterator

A non iterable class
"""


class NotIterableInt:
    """This class is not iterable, it does not implement __getitem__ nor __iter__ """

    def __init__(self, value):
        self._value = value
        self._buffer = str(value)

    def __repr__(self):
        return f"NotIterableInt({self._value})"


digits = NotIterableInt(347_123_348_922)
print(digits)

try:
    # not iterable
    iter(NotIterableInt(42))
except TypeError as ex:
    print(ex)
