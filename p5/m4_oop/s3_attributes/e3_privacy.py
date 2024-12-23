"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Attributes and properties - privacy (kind of)
"""


class A:
    """A class with some kind of privatness"""

    def __init__(self):
        # please, do not access this attribute
        self._internal_detail = 42
        # you really should not access this attribute
        self.__more_internal_detail = 99


a = A()

# accessing an underscored attribute is easy
print("The internal detail is", a._internal_detail)

# accessing a double underscored attribute is a bit less immediate
# mangling: the attribute name is prefixed with an underscore and the class name
print("The more internal detail is", a._A__more_internal_detail)
