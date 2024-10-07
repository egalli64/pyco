"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

String literals
Single char
"""

# a Python char is a string sized 1
s_x = "x"
print(type(s_x), s_x, "- no char type in Python, just a string sized one")

# get the Unicode code point representation of a char
code_x = ord(s_x)
print(type(code_x), code_x, "- Unicode")

# the integer representation for the Unicode code point of a grinning face
code_grin = 0x1F600
s5 = chr(code_grin)
print("Grin hex Unicode and its character representation:", hex(code_grin), s5)

# escape sequences
s6 = "a multiline string\n\tis 'useful' to represent \"long\" text\nthat should be read by humans"
print(s6)
