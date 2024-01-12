"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Numeric Types

complex
"""
z = 2.7 + 4.2j
print(f"A complex {z} has type {type(z)}")
print(f"Its real part is {z.real} ({type(z.real)})")
print(f"And its imaginary part is {z.imag} ({type(z.real)})")
print("Its conjugate is", z.conjugate())

z2 = complex(2.7, 4.2)
if z == z2:
    print("Two different way to express the same complex number", z2)
