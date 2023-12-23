"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 6 - Modules and Packages

A script that imports modules from other packages
"""
import sys

# import from a direct sub-package a couple of modules
from sub import alpha, beta

# import from a sub-sub-package another module
from sub.deeper import delta as d

# import a function in a module in a sub-sub-package
from sub.deeper.gamma import check as g_check

if __name__ == "__main__":
    print(f"From {__name__} accessing alpha")
    alpha.check()

    print(f"From {__name__} accessing beta")
    beta.check()

    print(f"From {__name__} accessing sub.deeper.delta")
    d.check()

    print(f"From {__name__} accessing sub.deeper.gamma")
    g_check()
