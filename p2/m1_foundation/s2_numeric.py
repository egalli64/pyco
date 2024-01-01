"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - More fundamental concepts

Numeric types
"""
import sys
import math

# integers
a = 42
b = 5

print("Integer division '//' vs float division '/':", end=" ")
print(f"a = {a}, b = {b}, a // b = {a // b}, a / b = {a / b}")

x = 2**1_000
print(f"An int, {type(x)}, could be very large: {x}\n")

# float
print(f"The epsilon between 1.0 and the next float is about {sys.float_info.epsilon}")
print("Beware of binary conversion approximation issues, 0.3 - 0.2 =", 0.3 - 0.2)

print(f"The smallest representable positive float is {sys.float_info.min}")
print(f"The largest representable positive float is {sys.float_info.max}")

too_big_pos = sys.float_info.max * 2
too_big_neg = sys.float_info.max * -2
print(f"Out of bound is infinite: {too_big_neg}, {too_big_pos}")
print("An undefined result is considered as Not-A-Number:", too_big_neg + too_big_pos)

print("Are both 'too_big_pos' and 'too_big_neg' infinite?", end=" ")
print(math.isinf(too_big_neg) and math.isinf(too_big_pos))
print("Is their sum nan?", math.isnan(too_big_neg + too_big_pos))
print()

# complex
z = 2.7 + 4.2j
print(f"A complex {z} has type {type(z)}")
print(f"Its real part is {z.real} and its imaginary part is {z.imag}")
print("Its conjugate is", z.conjugate())
