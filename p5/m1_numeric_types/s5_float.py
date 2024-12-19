"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 1 - Numeric Types

float
"""

import math
import sys

# float literals
x = 123_456.789e18
print(f"x is {x} {type(x)}\n")

# different literal representations
x = 2_000.0
y = 2e3
if x == y:
    print("The same value could be expressed in plain or exponential format")

# approximation
x = 0.3
y = 0.2
print(f"Beware of binary conversion approximation issues, {x} - {y} = {x-y}\n")


# a few constants
print(f"The epsilon between 1.0 and the next float is about {sys.float_info.epsilon}")
print(f"The smallest representable positive float is {sys.float_info.min}")
print(f"The largest representable positive float is {sys.float_info.max}")
print()

# close enough?
print("Check if close enough using default difference")
for delta in (0.000_000_003, 0.000_000_004):
    x = math.pi + delta
    print(f"Is {math.pi} close enough to {x}?", math.isclose(math.pi, x))
print()

# infinite
print(f"Achieving infinite in different ways: {math.inf}, {float('inf')}")
print(f"Achieving -infinite in different ways: {-math.inf}, {float('-inf')}")

x = sys.float_info.max * -2
y = sys.float_info.max * 2
print(f"Out of bound is infinite: {x}, {y}")

print(f"Are both 'x' {x} and 'y' {y} infinite?", end=" ")
print(math.isinf(x) and math.isinf(y))

# nan
print(f"\nAchieving 'not a number' in different ways: {math.nan}, {float('nan')}")

# undefined result as nan
z = x + y
print(f"Is {x} + {y} equal to {math.nan}?", math.isnan(z))
