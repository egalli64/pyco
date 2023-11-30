"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 5 - Function

Return value
"""


def noop():
    """A function that has no parameter and no return value"""
    pass


# calling noop we get None as result
result = noop()
print(result, type(result))


def noop2():
    """A function that explicitly has no return value"""
    return None


# calling noop2 we still get None as result
result = noop2()
print(result, type(result))


def solution():
    """A function taking no argument and always returning the same integer"""
    return 42


# calling solution we get an int
result = solution()
print(result, type(result))


def is_even(value):
    """A function with two possible return values"""
    if value % 2 == 0:
        return True
        # code after a return in the same control flow is "dead code"
        # print("This is not good")
    else:
        return False


# calling is_even we get a bool: True or False
result = is_even(solution())
print(result, type(result))
