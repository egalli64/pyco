"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

Property
"""


class A:
    """A class with internal details that I'd like stay in it"""

    def __init__(self):
        self._internal_detail = 42
        self.__more_internal_detail = 99

    @property
    def more_internal_detail(self):
        """__more_internal_detail getter as more_internal_detail"""
        print("getter at work")
        return self.__more_internal_detail

    @more_internal_detail.setter
    def more_internal_detail(self, reset):
        """__more_internal_detail setter as more_internal_detail"""
        print("setter at work")
        self.__more_internal_detail = reset

    @property
    def calculated_sum(self):
        """A calculated property"""
        return self._internal_detail + self.__more_internal_detail


a = A()

# accessing an underscored attribute is easy
print("The internal detail is", a._internal_detail)
# accessing a double underscored attribute is a bit less immediate
print("The more internal detail is", a._A__more_internal_detail)

# using getter and setter
print("The more internal detail is", a.more_internal_detail)
a.more_internal_detail = 12
print("The more_internal_detail has changed")
print("Now the more internal detail is", a.more_internal_detail)

# accessing the calculated property
print("The calculated sum is", a.calculated_sum)

try:
    a.calculated_sum = 42
except AttributeError as ex:
    print(ex)
