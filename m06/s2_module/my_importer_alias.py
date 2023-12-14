"""
Python Course

https://github.com/egalli64/pyco

Module 6 - Modules and Packages

Import from a module
"""
from m06.s2_module.a_module import greeting
from m06.s2_module.a_module import APPLICATION_NAME as NAME

# calling a function defined in the imported module
greeting("Tom")

# accessing a variable (constant) defined in the imported module
print("The application name is", NAME)
