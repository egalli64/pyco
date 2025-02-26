"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 3 - Concurrency

Asynchronous Programming: async def, await
"""


async def greet():
    """A coroutine is kind of a generator"""
    print("Hello", end=", ")
    # await pauses the current code execution
    # kind of similar to yield, but do not return to the caller
    # await for the result of the awaitable
    result = await something_required()
    print(f"[{result}]", end=" ")
    print("World")
    return "Done"


async def something_required():
    """Another coroutine"""
    return "..."


# the even loop manages asynchronicity and presents the code in a more natural way
cr = greet()
try:
    # the event loop would pass the context (here None)
    cr.send(None)
except StopIteration as ex:
    print(f"Coroutine returned: {ex.value}")
