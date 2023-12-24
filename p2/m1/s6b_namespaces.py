"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 1 - More on functions

Namespaces
"""
import s6a_module as m

# x defined in the current global scope
x = 42

# different global scopes could contains items with the same name
print("x in the current global scope plus x in another module global scope:", end=" ")
print(x + m.x)

# looking to what is in the current global scope
print("\nThe current global scope contains:")
for k, v in globals().copy().items():
    if k == "__doc__":
        print(f"*** {k} skipped ***")
    else:
        print(f"{k}: {v}")
print()


def f():
    """Confusing! the local x hides the global one!"""
    x = 99
    print("Inside function f(), the local namespace is", locals())
    print("In f() x is", x)


def g(a):
    # comment the next line to get an UnboundLocalError
    global x

    print("Inside function g(), the local namespace is", locals())
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

    print("Inside function h(), the local namespace is", locals())
    inner()
    print("Now local x in h() is", x)


f()
print(f"The global x is still {x}\n")

g("hello")
print(f"Now the global x is {x}\n")

h()
print("The global x is still", x)
