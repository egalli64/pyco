"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - Numeric Types

Builtin functions on numbers
"""
b1 = False
b2 = True

i1 = -6
i2 = 37
i3 = 8

f1 = -2.7
f2 = 25.357
f3 = 8.8

c1 = -8.3 - 4.1j
c2 = 5.9 + 7.2j
c3 = 3.6 + 2.4j

print("abs()")
print(" on bool:", abs(b1), abs(b2))
print(" on int:", abs(i1), abs(i2))
print(" on float:", abs(f1), abs(f2))
print(" on complex:", abs(c1), abs(c2))
print()

print("divmod()")
print(" on bool:", divmod(b1, b2))
print(" on int:", divmod(i2, i3))
print(" on float:", divmod(f2, f3))
print(" on int/float:", divmod(i2, f3))
try:
    divmod(c2, c3)
except TypeError as ex:
    print("", ex)
finally:
    print()

print("pow(base, exp)")
print(" on bool:", pow(b1, b2))
print(" on int:", pow(i1, i3))
print(" on float:", pow(f1, f3))
print(" on complex:", pow(c2, c3))
print()

print("pow(base, exp, mod)")
print(" on bool:", pow(b2, b1, b2))
print(" on int:", pow(i2, i3, i1))
try:
    pow(f1, f2, f3)
except TypeError as ex:
    print("", ex)
try:
    pow(c1, c2, c3)
except ValueError as ex:
    print("", ex)
    print()

print("round()")
print(" on bool:", round(b2), round(b2, -1))
print(" on int:", round(i2), round(i2, -1))
print(" on float:", round(f2), round(f2, 2))
try:
    round(c1)
except TypeError as ex:
    print("", ex)
print()
