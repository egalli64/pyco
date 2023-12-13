"""
Python Course

https://github.com/egalli64/pyco

Module 6 - Modules and Packages

Import a module using alias
"""
import my_module as my

# calling a function defined in the imported module
my.greeting("Tom")

# accessing a variable (constant) defined in the imported module
print("The application name is", my.APPLICATION_NAME)
