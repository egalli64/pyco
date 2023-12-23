"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 7 - Object Oriented Programming

Class and object
"""


class Empty:
    """Definition of an empty class"""


# instantiate an object of the Empty class
empty = Empty()

# using the Empty object
print(empty)


class Minimal:
    """Define a minimal class"""

    # uncommon, see __init__ usage
    attribute = "a value"

    def method(self):
        """A minimal method"""
        print("The method has been called")


# instantiate objects of the Minimal class
mini_1 = Minimal()
mini_2 = Minimal()

# accessing the attribute of Minimal objects
mini_1.attribute = "one"

print("mini_1 attribute is:", mini_1.attribute)
print("mini_2 attribute is:", mini_2.attribute)

# invoking the method on a Minimal object
mini_2.method()
