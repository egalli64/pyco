"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 1 - Fundamental concepts

String literals
"""

s1 = 'a string'
print(type(s1), s1)

s2 = "another string"
print(type(s2), s2)

s3 = """a multiline string
is useful for representing a long text
that should be read by humans"""
print(type(s3), s3)

# a Python char is a string sized 1
s4 = 'x'
print(type(s4), s4)

# get the Unicode code point representation of a char
code_x = ord(s4)
print(type(code_x), code_x)

# the integer representation for the Unicode code point of a grinning face
code_grin = 0x1F600
s5 = chr(code_grin)
print("A Unicode code and its associated character:", hex(code_grin), s5)

# escape sequences
s6 = "a multiline string\nis useful for representing a long text\nthat should be read by humans"
print(s6)

# f-string
PI = 3.141592653589793
radius = 5

print(f"A circle with radius {radius} has area {PI * radius ** 2}")
print(f"A pi approximation: {PI:.5f}")
