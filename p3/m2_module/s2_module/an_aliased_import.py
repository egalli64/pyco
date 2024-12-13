"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Module

Import a module with alias
"""
import a_module as am

# calling a function defined in the imported module
am.greeting("Tom")

# accessing a variable (constant) defined in the imported module
print("The application name is", am.APPLICATION_NAME)
