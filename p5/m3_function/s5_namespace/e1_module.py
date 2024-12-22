"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 3 - Function

Namespaces - a module meant to be imported
"""

# x defined in the current global scope
x = 21

if __name__ == "__main__":
    print("Beside dunders, the current global scope contains", end=" ")
    for k, v in globals().copy().items():
        if not k.startswith("__"):
            print(f"{k}={v}")
