"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Exception - try / finally
"""

import random


def resource_manager(x):
    try:
        print("Open and use a resource for", x)
        if random.random() > 0.5:
            raise Exception("A generic exception")
    finally:
        print("Close the resource")


for i in range(3):
    try:
        resource_manager(i)
    except:
        print("*** Trouble ***")
    else:
        print("OK")
