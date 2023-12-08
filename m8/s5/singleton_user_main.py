"""
Python Course

https://github.com/egalli64/pyco

Module 8 - Design Pattern

Singleton (by module)
"""
import singleton
from singleton_user_other import singleton_increaser

if __name__ == "__main__":
    singleton.value = 42
    print("Singleton has value", singleton.value)

    singleton_increaser()
    print("Singleton has value", singleton.value)
