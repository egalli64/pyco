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


# an integer is assigned to result
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


# a boolean is assigned to result
result = is_even(solution())
print(result, type(result))


def prev_next(value):
    """A function returning a tuple"""
    return (value-1, value+1)


# a tuple is assigned to result
result = prev_next(solution())
print(result, type(result))
