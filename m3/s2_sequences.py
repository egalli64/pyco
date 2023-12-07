"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 3 - List

Sequences
"""
# looping on three sequences
for seq in ["bob", "tom", "kim"], ("dan", "h", "jim"), "meh":
    print("A sequence:", seq)

    # len() accepts any sequence
    print("Its length is", len(seq))

    # access by index to its first element
    print("Its first element is", seq[0])

    # access by index to its last element
    print("Its last element is", seq[-1])

    # access by index to a non-existing element
    try:
        print(seq[42])
    except IndexError as ex:
        print("Bad!", ex)

    # looking for the index of a value
    try:
        target = "h"
        pos = seq.index(target)
        print(f"{target} found at {pos}")
    except ValueError as ex:
        print("No index,", ex)

    # concatenation is only for compatible types
    match seq:
        case list():
            other = ["zoe", "abe"]
        case tuple():
            other = ("zoe", "abe")
        case _:
            other = "ta"
    print("Concat:", seq + other)

    # repetition
    print("Repetition:", seq * 2)

    # operator (not) in
    if "h" in seq:
        print("element 'h' is in the sequence!")

    if "h" not in seq:
        print("element 'h' is not in the sequence!")
