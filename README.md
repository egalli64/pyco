# pyco - Python course
Developed on Python 3.12 - <https://www.python.org/downloads/>

## Part 1 - Fundamental concepts

### 1 - Foundation
    IO: print() and input()
    Variables
    Objects and types
    Dynamic typing and None
### 2 - The string data type
    Literal string, f-string, r-string
    String as iterable - accessed by iterator (for-in)
    String as immutable sequence: operator [], method index(), operator in
    Slicing on string (immutable sequences)
    Concatenation and repetition by + and *
    Some commonly used string methods
### 3 - Numeric types
    bool, int, float
    Cast to a numeric type
    Arithmetic operators
    Assignment operators
    Precedence and associativity
    Relational operators
    Logical operators
### 4 - Control Flow
    Compound instructions, indentation, pass
    Conditional statements: if - elif - else
    Conditional expression: if - else
    While loop
    For loop - the range() builtin function
    Jump in loop by break, continue, return
    Else in a loop statement

## Part 2 - Basic Data Structures

### 1 - List
    Mutable resizable sequence implementing the array ADT
    Literal definition
    Editing by methods and statement del
    Ordering by builtin sorted() and method sort()
    Unordering by random shuffle(), reversing by method reverse()
    List comprehension
### 2 - Tuple
    Kind of an immutable list
    Literal definition
    (Kind of) Tuple comprehension
### 3 - Dictionary
    Mutable collection of key-value pairs implementing the hashtable ADT
    Literal definition, constructor function, dictionary comprehension
    Accessing components by operator (not) in, [], method get()
    Editing components
    Views by items(), keys(), values()
    Copies by copy(), dict(), deepcopy()
    Update and merge
### 4 - Set
    Kind of a dictionary but with key-only elements
    Literal definition, constructor function, set comprehension
    Set as iterable: len(), (not) in, for-in
    Set editing
    Set theory

## Part 3 - Modularization

### 1 - Function
    Definition: header and body, docstring, pass
    Parameters and arguments
    Passing arguments by position and by name
    Default parameter value
    Varargs and argument unpacking
    Return value, or None
    Using iterators: iter(), next()
    Functional programming support
    Lambda expression as helper for map(), filter(), and sort()
### 2 - Module
    Import, from, as
    Search path: sys.path, PYTHONPATH
    Module __name__, the __main__ module
    Package, import module from package
### 3 - Object Oriented Programming
    Class: header and body
    Class body: docstring, attributes, methods
    Object: constructor and initializer
    Method: the self parameter
    The __init__ dunder
    The dot '.' operator
    Inheritance, super(), override
    Classes relation by issubclass()
    Object/class relation by isinstance()
    Exception: raise, try, except

## Part 4 - Files

### 1 - File
    open() / close(), with
    print(), write()
    read(), readlines(), readline(), for - in
    pathlib.Path
### 2 - Structured File
    CSV
    JSON

## Part 5 - More advanced topics

### 1 - Numbers
    The Number hierarchy
    Built-in types: bool, int, float, complex
    Boolean: True/Truthy, False/Falsy; and, or, not, exor
    Integer: binary, octal, hexadecimal; underscore; division; module; power

### 2 - More on function
    Inner function
    Closure
    Decorator
    Namespace, scope
### 3 - More on Object Oriented Programming
    Classes object and type
    Attributes and properties
    Method: instance, class, static
    Special methods: __init__(), ...
    Multiple Inheritance: __bases__
    Method Resolution Order: mro() and __mro__
    Abstract class and @abstractmethod
### 4 - Sequences
    Iterables and iterators: __getitem__, __iter__, __next__
    Generator: yield, comprehension
    collections.abc: Iterable, Sized, Container, Reversible, Collection, Sequence
    Comprehension and generator for sequence definition
    Unpacking on iterables
### 5 - Log and Test
    Log: print() on stderr
    logging: getLogger(), debug(), ..., basicConfig()
    Unit Test
    unittest: assertions, discover tests
    VS Code and unittest
### 6 - Design Patterns
    Singleton
    Factory Method
### 7 - ...
    Some builtin numeric functions
    float: epsilon, min, max, inf, nan
    complex: real, imag, conjugate()
    Chained comparison, implicit cast to boolean
    Conditional expressions: if-else, or, and
    string: slice, split(), join(), int to str
    Create list by zip()
    collections.namedtuple
