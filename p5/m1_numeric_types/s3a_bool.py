"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 1 - Numeric Types

bool
"""

flag = True
print("flag is", flag, type(flag))

x = 42
if x != True:
    print(f"Only 1 is True! {x} is {x == True}")

if x:
    print(f"But a non-zero number is truthy! {x} is {bool(x)}")

x = 0.0
if not x:
    print(f"A zero number, {x}, is false")

x = "0"
if x:
    print(f"A non-empty string, '{x}', is truthy")

x = ""
if not x:
    print(f"An empty string, '{x}', is falsy")


class ZeroSized:
    def __len__(self):
        return 0


x = ZeroSized()
if not x:
    print(f"An object with len 0 is falsy: len x is {len(x)}, bool x is {bool(x)}")


class FalseBool:
    def __bool__(self):
        return False


x = FalseBool()
if not x:
    print("An object False when cast to bool is falsy")


class Empty:
    pass


x = Empty()
if x:
    print("An object that does not define __bool()__ nor __len()__ is truthy")

x = None
if not x:
    print(f"None, {x}, is falsy")
