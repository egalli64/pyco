"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - Numeric Types

float
"""
import math
import sys

# float literals
f = 123_456.789e18
print("f is", f, type(f), "\n")

if 2_000.0 == 2e3:
    print("The same value could be expressed in plain or exponential format")

# a few constants
print(f"The epsilon between 1.0 and the next float is about {sys.float_info.epsilon}")
print("Beware of binary conversion approximation issues, 0.3 - 0.2 =", 0.3 - 0.2)
print(f"The smallest representable positive float is {sys.float_info.min}")
print(f"The largest representable positive float is {sys.float_info.max}")
print()

# close enough?
g = math.pi + 0.000_000_003
print(f"Is {math.pi} close (default) to {g}?", math.isclose(math.pi, g))
print()

# infinite
too_big_pos = sys.float_info.max * 2
too_big_neg = sys.float_info.max * -2
print(f"Out of bound is infinite: {too_big_neg}, {too_big_pos}")

print("An undefined result is considered as Not-A-Number:", too_big_neg + too_big_pos)

print("Are both 'too_big_pos' and 'too_big_neg' infinite?", end=" ")
print(math.isinf(too_big_neg) and math.isinf(too_big_pos))
print(f"Is their sum {math.nan}?", math.isnan(too_big_neg + too_big_pos))
print()

print("Achieving infinite in different ways:", math.inf, float("inf"))
print("Achieving -infinite in different ways:", -math.inf, float("-inf"))
print("Achieving nan in different ways:", math.nan, float("nan"))
