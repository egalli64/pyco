"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Closure - An example
"""


def closure_factory(x):
    """Generate a closure on the passed argument"""

    def closure(y):
        """Capture the outer parameter and accept an argument from the caller"""
        print(f"The closure captured '{x}' and recieved '{y}' as argument")

    return closure


# getting a closure
func = closure_factory("Hello")

# invoking a closure - just like any function
func("Tom")
func("Bob")

try:
    # the inner function can't be seen outside the function where it is defined
    closure("Jim")
except NameError as e:
    print("Can't see an inner function outside its definition scope:", e)
