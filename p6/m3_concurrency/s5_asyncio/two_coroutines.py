"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

Asynchronous Programming: two coroutines for the examples
"""

import asyncio
import random


async def numbering():
    """A coroutine priting numbers in [0, 10) waiting randomly for [0.0, 1.0) secs"""
    for i in range(10):
        await asyncio.sleep(random.random())
        print(i, end=" ", flush=True)
    return "Done numbering"


async def lettering():
    """A coroutine priting letters in [A, K) waiting randomly for [0.0, 1.0) secs"""
    base = ord("A")
    for i in range(base, base + 10):
        await asyncio.sleep(random.random())
        print(chr(i), end=" ", flush=True)
    return "Done lettering"
