"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 4 - Object Oriented Programming

Inheritance
"""


class Dog:
    """A barking dog"""

    def __init__(self, name):
        """
        Each dog has a name

        As the other methods, __init__ is inherited by the derived classes, if not overridden
        """
        self.name = name

    def bark(self):
        """Let the dog bark"""
        print(f"{self.name}: bark!")


class Spaniel(Dog):
    """
    Spaniel is-a Dog

    no __init__ provided, the Dog one is available as Spaniel's initializer
    """

    def run(self):
        """This is a specific Spaniel method"""
        print(f"{self.name} is running")


class Poodle(Dog):
    """Poodle is-a Dog"""

    def __init__(self, name, curl_density):
        """
        Each poodle has also a curl density

        The Dog __init__ is not available as Poodle initializer
        """
        super().__init__(name)
        self.curl_density = curl_density

    def bark(self):
        """
        Let the poodle bark

        Override the Dog bark(), polymorphism
        """
        print(f"{self.name}: bark in a curly way ({self.curl_density})")

    def just_bark(self):
        """Bypass the poodle bark override"""
        super().bark()


bob = Dog("Bob")
bob.bark()

jim = Spaniel("Jim")
jim.bark()
jim.run()

# won't work, TypeError: Poodle.__init__() missing 1 required positional argument: 'curl_density'
# tim = Poodle("Tim")

tom = Poodle("Tom", 0.27)
tom.bark()
tom.just_bark()

# check is-a relation between classed by issubclass
print("Is Spaniel a subclass of Dog?", issubclass(Spaniel, Dog))  # True
print("Is Spaniel a subclass of Poodle?", issubclass(Spaniel, Poodle))  # False

# check is-a relation of an object by isinstance
print("Is jim a Spaniel?", isinstance(jim, Spaniel))  # True
print("Is jim a Poodle?", isinstance(jim, Poodle))  # False
print("Is jim a Dog?", isinstance(jim, Dog))  # True
