"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 8 - Object Oriented Programming

Inheritance
"""


class Dog:
    """A barking dog"""

    def __init__(self, name):
        """Each dog has a name"""
        self.name = name

    def bark(self):
        """Let the dog bark"""
        print(f"{self.name}: bark!")


class Poodle(Dog):
    """Poodle is-a Dog"""

    def __init__(self, name, curl_density):
        """Each poodle has also a curl density"""
        super().__init__(name)
        self.curl_density = curl_density

    def bark(self):
        """Let the poodle bark"""
        print(f"{self.name}: bark in a curly way ({self.curl_density})")

    def just_bark(self):
        """Bypass the poodle bark override"""
        super().bark()


class Spaniel(Dog):
    """Spaniel is-a Dog"""

    def run(self):
        print(f"{self.name} is running")


bob = Dog("Bob")
bob.bark()

tom = Poodle("Tom", 0.27)
tom.bark()
tom.just_bark()

jim = Spaniel("Jim")
jim.bark()
jim.run()

# check is-a relation between classed by issubclass
print("Is Spaniel a subclass of Dog?", issubclass(Spaniel, Dog))
print("Is Spaniel a subclass of Poodle?", issubclass(Spaniel, Poodle))

# check is-a relation of an object by isinstance
print("Is jim a Spaniel?", isinstance(jim, Spaniel))
print("Is jim a Poodle?", isinstance(jim, Poodle))
print("Is jim a Dog?", isinstance(jim, Dog))
