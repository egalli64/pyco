"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 1 - Numeric Types

The Number hierarchy
"""

from numbers import Number, Complex, Real, Rational
from fractions import Fraction
from decimal import Decimal


# complex
x = 42 + 2j
print(f"Is {x} complex?", isinstance(x, complex), end=", ")
print("Complex?", isinstance(x, Complex), end=", ")
print("Number?", isinstance(x, Number))

# float
x = 42.7
print(f"Is {x} float?", isinstance(x, float), end=", ")
print("Real?", isinstance(x, Real), end=", ")
print("Number?", isinstance(x, Number))

# Fraction
x = Fraction(7, 3)
print(f"Is {x} Fraction?", isinstance(x, Fraction), end=", ")
print("Rational?", isinstance(x, Rational), end=", ")
print("Real?", isinstance(x, Real), end=", ")
print("Number?", isinstance(x, Number))

# int
x = 42
print(f"Is {x} int?", isinstance(x, int), end=", ")
print("Rational?", isinstance(x, Rational), end=", ")
print("Real?", isinstance(x, Real), end=", ")
print("Number?", isinstance(x, Number))

# Decimal
x = Decimal("3.14")
print(f"Is {x} Decimal?", isinstance(x, Decimal), end=", ")
print("Is Real?", isinstance(x, Real), end=" (NOT!), ")
print("Is Number?", isinstance(x, Number))

# bool
x = True
print(f"Is {x} bool?", isinstance(x, bool), end=", ")
print("int?", isinstance(x, int), end=", ")
print("Rational?", isinstance(x, Rational), end=", ")
print("Real?", isinstance(x, Real), end=", ")
print("Number?", isinstance(x, Number))
