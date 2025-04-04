"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Exception - stack unwinding until the script is terminated
"""


def raiser(s):
    """A function that always raise an exception"""
    if s != "42":
        raise ValueError(f"Didn't expect {s} as argument value")
    else:
        print(f"Using {s} to produce the solution")


def internal_detail():
    # ValueError expected
    raiser("hello")


def main():
    # ValueError expected
    internal_detail()


if __name__ == "__main__":
    # ValueError expected
    main()
    print("This statement should not be executed")
