"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 5 - Iterators

Unpacking
The * operator on arguments
"""

xs = [1, 2, 3, 4]
print("Given a list:", xs)


# 1a. a function with four parameters
def func(a, b, c, d):
    print(f"The func() parameters are: a={a}, b={b}, c={c}, and d={d}")


# 1b. unpack a list as argument
print("Passing the list (unpacked) to a function")
func(*xs)
print()

# 2a. unpack a tuple as argument
point = (53, 12)
print("Given a tuple:", point)

print("Passing the tuple (unpacked) to divmod()")
div, mod = divmod(*point)
print(f"{point[0]} // {point[1]} =", div)
print(f"{point[0]} % {point[1]} =", mod)
