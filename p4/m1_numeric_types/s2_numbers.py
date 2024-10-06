"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - Numeric Types

The Number hierarchy
"""
from numbers import Number, Complex, Real, Rational
from fractions import Fraction
from decimal import Decimal


# complex
x = 42 + 2j
print(x, "is a complex?", isinstance(x, complex))
print("Is a Complex?", isinstance(x, Complex))
print("Is a Number?", isinstance(x, Number), "\n")

# float
x = 42.7
print(x, "is a float?", isinstance(x, float))
print("Is a Real?", isinstance(x, Real))
print("Is a Number?", isinstance(x, Number), "\n")

# Fraction
x = Fraction(7, 3)
print(x, "is a Fraction?", isinstance(x, Fraction))
print("Is a Rational?", isinstance(x, Rational))
print("Is a Real?", isinstance(x, Real))
print("Is a Number?", isinstance(x, Number), "\n")

# int
x = 42
print(x, "is an int?", isinstance(x, int))
print("Is a Rational?", isinstance(x, Rational))
print("Is a Real?", isinstance(x, Real))
print("Is a Number?", isinstance(x, Number), "\n")

# Decimal
x = Decimal("3.14")
print(x, "is a Decimal?", isinstance(x, Decimal))
print("Is _not_ a Real?", not isinstance(x, Real))
print("Is a Number?", isinstance(x, Number), "\n")

# bool
x = True
print(x, "is a bool?", isinstance(x, bool))
print("Is an int?", isinstance(x, int))
print("Is a Rational?", isinstance(x, Rational))
print("Is a Real?", isinstance(x, Real))
print("Is a Number?", isinstance(x, Number), "\n")
