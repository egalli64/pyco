"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

Asynchronous Programming: asyncio gather()
"""

import asyncio
from two_coroutines import numbering, lettering


async def main():
    """gather two tasks to run them concurrently"""
    result = await asyncio.gather(numbering(), lettering())
    print()
    return result


result = asyncio.run(main())
print("Gathered result:", result)
