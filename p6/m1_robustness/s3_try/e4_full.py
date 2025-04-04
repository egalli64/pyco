"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Exception
"""

import math

for x in -1.0, 1.0:
    try:
        result = math.sqrt(x)
    except ValueError as e:
        print(f"Can't calculate square root of {x}:", e)
    else:
        print(f"Square root of {x} is", math.sqrt(x))
    finally:
        print("*** Done ***")
