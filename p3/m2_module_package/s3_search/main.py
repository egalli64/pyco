"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Modules and Packages

Module search path
"""

import sys
import csv

try:
    # this module is not expected to exist
    import a_missing_module
except ModuleNotFoundError as ex:
    print("ModuleNotFoundError:", ex)

# highest priority modules
print("The built-in modules:", sys.builtin_module_names)

# paths for the (other) modules that could be imported
print("The current module search path:")
for current in sys.path:
    print(current)

try:
    print(csv.__version__)
except AttributeError as ex:
    print("What's going on? -->", ex)
