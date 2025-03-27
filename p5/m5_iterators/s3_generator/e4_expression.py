"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Generator expression
"""

# define a generator by expression
gen = (x**2 for x in range(10))

print("Use a generator (by expression) in a for-in", end=": ")
for cur in gen:
    print(cur, end=" ")
print()

# (re) define a generator by expression
gen = (x**2 for x in range(10))

print("Use a generator (by expression) in a while loop", end=": ")
while True:
    try:
        print(next(gen), end=" ")
    except StopIteration:
        print()
        break
