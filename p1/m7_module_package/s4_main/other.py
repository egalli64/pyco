"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 7 - Modules and Packages

Another module
"""
import main as m


def fun():
    print("Some misterious stuff is done in module", __name__)


if __name__ == "__main__":
    m.greeting("stranger")

    print("The normal access to this program is through the main module")
    fun()
    print("Bye")
