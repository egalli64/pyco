"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

Asynchronous Programming: asyncio create_task()
"""

import asyncio
from two_coroutines import numbering, lettering


async def concurrent_print():
    """create the two tasks, let run them concurrently"""
    task1 = asyncio.create_task(numbering())
    task2 = asyncio.create_task(lettering())

    # ensure both tasks are terminated before returning
    r1 = await task1
    r2 = await task2
    print()
    return r1, r2


async def sequential_print():
    """create the two tasks, await the end of the first before run the second one"""
    r1 = await numbering()
    r2 = await lettering()
    print()
    return r1, r2


print("Concurrent by create_task()")
result = asyncio.run(concurrent_print())
print(result)

print("Sequential by await")
result = asyncio.run(sequential_print())
print(result)
