"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 3 - List

Sequences - basic functionality
"""
seq = ["bob", "tom", "kim"]
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
for target in "tim", "tom":
    try:
        pos = seq.index(target)
        print(f"{target} found at {pos}")
    except ValueError as ex:
        print("No index,", ex)

# operator (not) in
if "tom" in seq:
    print("element 'tom' is in the sequence!")

if "tim" not in seq:
    print("element 'tim' is not in the sequence!")

# concatenation is only between compatible types
print("Concat:", seq + ["zoe", "abe"])

# repetition
print("Repetition:", seq * 2)
