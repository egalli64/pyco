"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Special methods - __len__()
"""


class Course:
    def __init__(self, name):
        """Each course has a name and a list of participants"""
        self.name = name
        self.participants = []

    def add(self, participant):
        """Add a new participant to the list"""
        print(f"{participant} enrolls in the {self.name} course")
        self.participants.append(participant)

    def __len__(self):
        """Returns the number of participants to the course"""
        return len(self.participants)


py = Course("Python")
py.add("Tom")
py.add("Bob")
py.add("Kim")

print(f"Number of {py.name} course participants:", len(py))
