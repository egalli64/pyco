"""
Python Course

https://github.com/egalli64/pyco

Module 3 - List

List comprehension
"""
# list of values in [1 .. 6]
dice = list(range(1, 7))
print(dice)


# list of squares
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

print(squares)

# list comprehension

# worst than the list-range approach, actually
dice_c = [x for x in range(1, 7)]
print(dice)

# this one is more interesting
squares_c = [x ** 2 for x in range(1, 11)]
print(squares_c)

# filter to get only even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# the external comprehension for rows, the internal one for columns
matrix = [[i + j for j in range(2)] for i in range(3)]
print(matrix)
