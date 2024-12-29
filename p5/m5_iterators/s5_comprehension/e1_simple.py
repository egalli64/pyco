"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Generator and list comprehension
Compare list comprehension vs initialization by for loop
"""
# list comprehension for values in [0, 100) divisible by 5 and 7
values = [x for x in range(0, 100, 5) if x % 7 == 0]
print(values)

# same, by for loop
values = []
for x in range(0, 100, 5):
    if x % 7 == 0:
        values.append(x)
print(values)
