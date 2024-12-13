"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Object Oriented Programming

Class and object
"""


class Empty:
    """Definition of an empty class"""


# instantiate an object of the Empty class
empty = Empty()

# using the Empty object
print("An empty object:", empty)


class Minimal:
    """Define a minimal class"""

    # this is a class attribute, not an instance one!
    attrib = "a value"

    def method(self):
        """A minimal method"""
        print("The minimal method has been called")


# instantiate objects of the Minimal class
mini_1 = Minimal()
mini_2 = Minimal()

# accessing a class attribute to change it
Minimal.attrib = "Yuck"

# accessing an instance attribute - it is created new, shadowing the class one!
mini_1.attrib = "one"

print("Minimal attrib is still:", Minimal.attrib)
print("mini_1 instance attrib is:", mini_1.attrib)
print("mini_2 has no attrib, fall back to Minimal attrib:", mini_2.attrib)

# invoking the method on a Minimal object
mini_2.method()
