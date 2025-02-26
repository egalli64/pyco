"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

Asynchronous Programming: asyncio run()
"""

import asyncio


async def worker():
    """A coroutine"""
    print("Worker task started")
    await asyncio.sleep(1)
    print("Worker task terminating")
    return "Done"


print("Switching to asynchronous code")
result = asyncio.run(worker())
print("Worker result:", result)
print("Getting back to synchronous code")
