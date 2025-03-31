"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Module

Filtered import from a module
"""

from a_module import greeting

# calling a function defined in the imported module
greeting("Tom")

try:
    # can't see APPLICATION_NAME definition (not imported!)
    print("The application name is", APPLICATION_NAME)
except NameError as e:
    print("NameError:", e)

print("Done")
