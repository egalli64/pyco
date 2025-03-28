"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 1 - Function

Return value
"""


def noop():
    """A function that has no parameter and no return value"""
    pass


# calling noop we get None as result
result = noop()
print("The value returned by noop() is", result)


def noop2():
    """A function that explicitly has no return value"""
    return None


# calling noop2 we still get None as result
result = noop2()
print("The value returned by noop2() is", result)


def solution():
    """A function taking no argument and always returning the same integer"""
    return 42


# an integer is assigned to result
result = solution()
print("The value returned by solution() is", result)


def is_even(value):
    """A function that accepts an int with two possible return values"""

    # verbose version
    # if value % 2 == 0:
    #     return True
    #     # code after a return in the same control flow is "dead code"
    #     print("This is not good")
    # else:
    #     return False

    # compact version
    # return True if value % 2 == 0 else False

    # even more compact
    return value % 2 == 0


# a boolean is assigned to result
result = is_even(solution())
print("The value returned by is_even() is", result)


def prev_next(value):
    """A function returning a tuple"""
    # the round brackets are not mandatory
    return value - 1, value + 1


# a tuple is assigned to result
result = prev_next(solution())
print("The value returned by prev_next() is", result, type(result))
