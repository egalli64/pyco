"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Modules and Packages

Plain import of a module
"""
import a_module

# calling a function defined in the imported module
a_module.greeting("Tom")

# accessing a variable (constant) defined in the imported module
print("The application name is", a_module.APPLICATION_NAME)
