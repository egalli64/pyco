"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 2 - Design Pattern

Singleton (by module)
"""
import singleton
from user_other import singleton_increaser

if __name__ == "__main__":
    singleton.value = 42
    print("Singleton has value", singleton.value)

    singleton_increaser()
    print("Singleton has value", singleton.value)
