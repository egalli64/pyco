"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Class decorator - An example
"""


class SimpleDecorator:
    """A callable class that decorates a function"""

    def __init__(self, func):
        """it captures 'func' and mantains an extra state"""
        self._func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        """it wraps the captured func with extra code"""
        self._count += 1
        print(f"Before the actual ({self._count}) function call")
        result = self._func(*args, **kwargs)
        print("After the actual function call")
        return result


# the decorated function is passed to the decorator ctor
@SimpleDecorator
def hello(name):
    print("Hello,", name)


print("Invoking the decorated function ...")
hello("Alice")
hello("Bob")
