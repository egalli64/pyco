"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Namespaces - a module that imports another module
"""

import e1_module as m

# x defined in the current global scope
x = 42


def f():
    """Confusing! the local x hides the global one!"""
    x = 99
    print("Inside function f(), the local namespace is", locals())
    print("In f(), x =", x)


def g(a):
    """This function has write access to global x"""
    # comment the next line to get an UnboundLocalError
    global x

    print("Inside function g(), the local namespace is", locals())
    print("In g(), parameter a =", a)
    try:
        x += 2
        print("Value of x changed in g()")
    except UnboundLocalError as ex:
        print("UnboundLocalError:", ex)


def h():
    """Very confusing! A local x hiding global x, modified by an inner function!"""
    x = 7
    print("In h(), local x =", x)

    def inner():
        # comment the next line to get an UnboundLocalError
        nonlocal x
        x += 5
        print("Value of nonlocal x changed in h-inner()")

    print("Inside function h(), the local namespace is", locals())
    inner()
    print("Now local x in h() is", x)


if __name__ == "__main__":
    # looking to what is in the current global scope
    print("1. Beside dunders, the current global scope contains ...")
    for k, v in globals().copy().items():
        if not k.startswith("__"):
            print(f"{k}: {v}")
    print()

    # different global scopes could contains items with the same name
    print(f"There's an x = {x} in the current global namespace")
    print(f"And an x = {m.x} in the module m global namespace")

    print("\n2. Calling f()")
    f()
    print(f"Back to the global scope, x = {x}")

    print("\n3. Calling g('hello')")
    g("hello")
    print(f"Back to the global scope, x = {x}")

    print("\n4. Calling h()")
    h()
    print(f"Back to the global scope, x = {x}")
