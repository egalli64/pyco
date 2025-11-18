"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

Math: rounding
"""
import math

print("Rounding pi and e by built-in round():", round(math.pi), round(math.e))
print("Ceil (closer to inf):", math.ceil(math.pi), math.ceil(math.e))
print("Trunc (closer to zero):", math.trunc(math.pi), math.trunc(math.e))
print("Floor (closer to -inf):", math.floor(math.pi), math.floor(math.e))

negPi = -math.pi
negE = -math.e

print("Rounding -pi and -e by built-in round():", round(negPi), round(negE))
print("Ceil (closer to inf):", math.ceil(negPi), math.ceil(negE))
print("Trunc (closer to zero):", math.trunc(negPi), math.trunc(negE))
print("Floor (closer to -inf):", math.floor(negPi), math.floor(negE))
