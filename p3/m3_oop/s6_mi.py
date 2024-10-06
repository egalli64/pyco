"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

Multiple Inheritance
"""


class Animal:
    def hello(self):
        print("Hello, I'm an animal!")


class Horse(Animal):
    def hello(self):
        print("Hello, I'm a horse!")


class Donkey(Animal):
    def hello(self):
        print("Hello, I'm a donkey!")


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


print("Method Resolution Orders:")
print("In a list:", Mule.mro())
print("In a tuple:", Mule.__mro__)
print(Hinny.mro())

print("Mule bases:", Mule.__bases__)
print("Hinny bases:", Hinny.__bases__)

print("A mule (is mainly a Donkey):", end=" ")
Mule().hello()

print("A hinny (is mainly a Horse):", end=" ")
Hinny().hello()


class RebelMule(Donkey, Horse):
    def hello(self):
        """Do not care about MRO, explictly call Animal hello()"""
        Animal.hello(self)


print("A rebel mule (is mainly a Donkey but doesn't care):", end=" ")
RebelMule().hello()
