"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Functional programming
"""


def greeter():
    """Definition of a simple function"""
    print("Hello from function greeter")


# A function is an object
print("The type of greeter is", type(greeter))

# invoking a simple function
greeter()


def runner(f):
    """Definition of a simple Higher-Order Function (HOF)"""
    print("This HOF runs the passed function:", end=" ")
    f()


# invoking a HOF
runner(greeter)


def runner2(f, left, right):
    """HOF for a function accepting two arguments"""
    print(f"This HOF runs the passed function on {left} and {right}:", end=" ")
    f(left, right)


def adder(left, right):
    """A simple function"""
    print("The adder function has been invoked:", left + right)


# invoking the adder function
adder(24, 18)
# passing the adder function to a HOF
runner2(adder, 24, 18)
