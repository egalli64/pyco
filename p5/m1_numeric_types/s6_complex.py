"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 1 - Numeric Types

complex
"""

x = 2.7 + 4.2j
print(f"A complex {x} has type {type(x)}")
print(f"Its real part is {x.real} {type(x.real)}")
print(f"And its imaginary part is {x.imag} {type(x.real)}")
print("Its conjugate is", x.conjugate())

y = complex(2.7, 4.2)
if x == y:
    print("Two different way to express the same complex number", y)
