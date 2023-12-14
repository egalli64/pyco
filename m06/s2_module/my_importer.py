"""
Python Course

https://github.com/egalli64/pyco

Module 6 - Modules and Packages

Import a module
"""
import m06.s2_module.a_module as a_module

# calling a function defined in the imported module
a_module.greeting("Tom")

# accessing a variable (constant) defined in the imported module
print("The application name is", a_module.APPLICATION_NAME)
