"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

Attributes and properties
"""


class A:
    # No docstring - bad idea, give the reader an idea of what this class is for

    # two class attributes
    x = 12
    # notice that an attribute has direct access to other attributes in the same scope
    y = x + 27

    def __init__(self):
        # an instance attribute - bad idea, I'm hiding the class attribute x
        # access to the class attribute both properly (by class reference) and confusingly (by self reference)
        # notice that there is no direct access to class or instance attributes
        self.x = A.y + self.y


print(f"Two class attributes in class A: {A.x}, {A.y}")
print("The class A docstring is:", A.__doc__)

a = A()
print(f"An instance attribute in object a: {a.x}")
print(f"Is this what I was expecting? {a.x}, {a.y}")
print(f"Probably I expected this result: {a.__class__.x}, {a.__class__.y}")


class B:
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


print("The class B docstring is:", B.__doc__)

b = B()

# accessing an underscored attribute is easy
print("The internal detail is", b._internal_detail)
# accessing a double underscored attribute is a bit less immediate
print("The more internal detail is", b._B__more_internal_detail)

# using getter and setter
print("The more internal detail is", b.more_internal_detail)
b.more_internal_detail = 12
print("The more_internal_detail has changed")
print("Now the more internal detail is", b.more_internal_detail)

# accessing the calculated property
print("The calculated sum is", b.calculated_sum)

try:
    b.calculated_sum = 42
except AttributeError as ex:
    print(ex)
