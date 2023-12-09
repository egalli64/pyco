"""
Python Course

https://github.com/egalli64/pyco

Module 9 - Design Pattern

Factory Method
"""
from factory_method import Base

for type in "Red", "Green", "Blue":
    try:
        x = Base.create(type)
        x.greeter()
    except ValueError as ex:
        print(ex)
