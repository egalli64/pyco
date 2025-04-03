"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

pickle - malicious dump
"""

import pickle
import os


class Malicious:
    def __reduce__(self):
        return (os.system, ("echo Doing something bad ...",))


with open("malicious.pkl", "wb") as file:
    pickle.dump(Malicious(), file)
