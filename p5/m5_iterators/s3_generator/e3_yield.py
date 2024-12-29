"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Generator

A generator with many yield in it
"""


def my_generator():
    yield "P"
    yield "y"
    yield "t"
    yield "h"
    yield "o"
    yield "n"


py_gen = my_generator()
for x in py_gen:
    print(x, end="")
