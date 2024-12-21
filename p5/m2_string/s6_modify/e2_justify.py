"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

Modify - justify to add padding
"""

s = "Hello, Python!"
print(f"The original string: {s}\n")

centered = s.center(20)
print(f"Center (default padding): _{centered}_")
print(f"Center (dot padding)    : _{s.center(20, '.')}_")
print(f"Left : {s.ljust(20, '_')}")
print(f"Right: {s.rjust(20, '_')}")
print(f"Zero : {s.zfill(20)}\n")

# strip is to remove padding
print(f"Left strip : _{centered.lstrip()}_")
print(f"Right strip: _{centered.rstrip()}_")
print(f"Full strip : _{centered.strip()}_")
