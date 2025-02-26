"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

Asynchronous Programming: asyncio run()
"""

import asyncio
from two_coroutines import lettering

# create a lettering coroutine and pass it to the event loop
print("To run a coroutine we need the event loop")
result = asyncio.run(lettering())
print("\nWorker result:", result)
