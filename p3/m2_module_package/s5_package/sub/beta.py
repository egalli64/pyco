"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 2 - Modules and Packages

A module that imports and sometime is imported
"""

if __name__ == "__main__":
    # when executed as script make absolute access the package below
    import deeper.delta as delta
else:
    # when loaded as module make relative access the package below
    from .deeper import delta


def check():
    print(f"From {__name__} accessing deeper.delta (level below - hybrid approach)")
    delta.check()


if __name__ == "__main__":
    check()
