"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Iterators - Generator

Using a generator when an iterator is an overkill
"""


def countdown(n):
    """A simple generator function"""
    while n > 0:
        yield n
        n -= 1


gen = countdown(5)

# Looping over a generator
print("Countdown by generator (for-in):", end=" ")
for cur in gen:
    print(cur, end=" ")
print()

# Iterating over a generator
print("Countdown by generator (iterating):", end=" ")
gen = countdown(5)
while True:
    try:
        print(next(gen), end=" ")
    except StopIteration:
        print()
        break
