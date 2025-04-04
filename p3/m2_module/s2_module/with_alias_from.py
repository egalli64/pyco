"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Module

Import a module using alias
"""

from a_module import greeting as am_greeter, APPLICATION_NAME as AM_NAME

# calling an aliased function defined in the imported module
am_greeter("Tom")

# accessing an aliased constant defined in the imported module
print("The application name is", AM_NAME)
