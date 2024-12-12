"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Modules and Packages

A module that imports and is imported
"""
if __name__ == "sub.deeper.gamma":
    # absolute access to a module two packages above 
    import epsilon
    # relative access to a module above
    from .. import beta
    # relative access to a module in the same package
    from .delta import check as d_check
else:
    print("This package should be imported from two packages above")


def check():
    print(f"From {__name__} accessing epsilon (absolute)")
    epsilon.check()

    print(f"From {__name__} accessing ..beta (relative, level above)")
    beta.check()

    print(f"From {__name__} accessing .delta (relative, same level)")
    d_check()
