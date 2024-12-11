"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 7 - Modules and Packages

A module that imports and is imported
"""
if __name__ == "sub.alpha":
    # the search path is on the package above
    import epsilon

    # relative access to beta, in the current package
    from .beta import check as b_check

    # absolute access to the package below
    import sub.deeper.delta as delta

    # relative access to the package below
    from .deeper.gamma import check as g_check
else:
    print("This package should be imported from the package above")


def check():
    print(f"From {__name__} accessing epsilon (absolute)")
    epsilon.check()

    print(f"From {__name__} accessing .beta (relative, same level)")
    b_check()

    print(f"From {__name__} accessing sub.deeper.delta (absolute)")
    delta.check()

    print(f"From {__name__} accessing .deeper.gamma (relative, level below)")
    g_check()
