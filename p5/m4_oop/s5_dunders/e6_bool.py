"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Special methods - __bool__()
"""


class Course:
    def __init__(self):
        """Each course has a list of participants"""
        self.participants = []


c1 = Course()

if c1:
    print("A course instance is always True")

class Course_2:
    def __init__(self):
        """Each course has a list of participants"""
        self.participants = []

    def __bool__(self):
        return bool(self.participants)

c2 = Course_2()

if not c2:
    print("An empty course_2 is False")

c2.participants.append("Bob")

if c2:
    print("A non-empty course_2 is True")
