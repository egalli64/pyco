"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 2 - String

String literals
Single char
"""
# a Python char is a string sized 1
s4 = "x"
print(type(s4), s4)

# get the Unicode code point representation of a char
code_x = ord(s4)
print(type(code_x), code_x)

# the integer representation for the Unicode code point of a grinning face
code_grin = 0x1F600
s5 = chr(code_grin)
print("A Unicode code and its associated character:", hex(code_grin), s5)

# escape sequences
s6 = "a multiline string\nis 'useful' to represent \"long\" text\nthat should be read by humans"
print(s6)
