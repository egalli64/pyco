"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Numeric Types

bool
"""
flag = True
print("flag is", flag, type(flag))

if 42 != True:
    print("Only 1 is True!")

if 42:
    print("A non-zero number is truthy")

if not 0.0:
    print("A zero number is false")

if "0":
    print("A non-empty string is truthy")

if not "":
    print("An empty string is falsy")


class ZeroSized:
    def __len__(self):
        return 0


if not ZeroSized():
    print("An object with len 0 is falsy")


class FalseBool:
    def __bool__(self):
        return False


if not FalseBool():
    print("An object False when casted to bool is falsy")
