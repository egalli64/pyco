"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Attributes and properties - instance attributes
"""


class A:
    """A class with class and instance attributes"""

    score = 12

    def __init__(self, score, name):
        # an instance attribute - bad idea, I'm hiding the class attribute with the same name
        self.score = score
        self.name = name


a = A(42, "Tom")
print("The class score:", A.score)
print("Accessing the class score an instance reference:", a.__class__.score)
print(f"The instance score '{a.score}' and name '{a.name}'")
