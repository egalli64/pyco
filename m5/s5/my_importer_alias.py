"""
Python Course

https://github.com/egalli64/pyco

Module 5 - Function

Import from a module
"""
from my_module import greeting
from my_module import APPLICATION_NAME as NAME

# calling a function defined in the imported module
greeting("Tom")

# accessing a variable (constant) defined in the imported module
print("The application name is", NAME)
