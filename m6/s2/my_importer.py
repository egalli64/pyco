"""
Python Course

https://github.com/egalli64/pyco

Module 6 - Module

Import a module
"""
import my_module

# calling a function defined in the imported module
my_module.greeting("Tom")

# accessing a variable (constant) defined in the imported module
print("The application name is", my_module.APPLICATION_NAME)
