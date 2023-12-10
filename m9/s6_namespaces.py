"""
Python Course

https://github.com/egalli64/pyco

Module 9 - More on functions

Namespaces
"""
import s6_module

# x defined in the current global scope
x = 42

# different global scopes could contains items with the same name
print("x in the current global scope plus x in another module global scope:", end=" ")
print(x + s6_module.x)

# looking to what is in the current global scope
print(globals())


def f():
    """Confusing! the local x hides the global one!"""
    x = 99
    print("The content of the local namespace:", locals())
    print("In f() x is", x)


def g(a):
    # comment the next line to get an UnboundLocalError
    global x

    print("The content of the local namespace:", locals())
    print(a)
    x += 2


def h():
    """Very confusing! A local x hiding global x, modified by an inner function!"""
    x = 7
    print("Local x in h() is", x)

    def inner():
        # comment the next line to get an UnboundLocalError
        nonlocal x
        x += 5
        print("nonlocal x in inner() changed to", x)

    print("The content of the local namespace:", locals())
    inner()
    print("Now local x in h() is", x)


f()
print("The global x is still", x)

g("hello")
print("Now the global x is", x)

h()
print("The global x is still", x)
