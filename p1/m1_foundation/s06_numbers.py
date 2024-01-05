"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 1 - Fundamental concepts

Numeric types
"""
# bool
flag = False
print("flag is", flag, type(flag))

# int
a = 4_200_238
print("a is", a, type(a))

flag = bool(a)
print("now flag is", flag)

print("the binary number 0b10 has decimal representation", 0b10)
print("the octal number 0o12345670 has decimal representation", 0o12345670)
print("the hexadecimal number 0x1234567890ABCDEF has decimal representation", end=" ")
print(0x1234567890ABCDEF)

# float
f = 123_456.789e18
print("f is", f, type(f))

# bool to float
f = float(flag)
print("now f is", f)

# int to float
f = float(a)
print("now f is", f)

# initial zeroes in a literal float are skipped
f = 04.2
print("and now is", f)
