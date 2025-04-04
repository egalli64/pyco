# pyco - Python course
Verified on Python 3.13 - <https://www.python.org/downloads/>

## Part 1 - Fundamental concepts

### 1 - Foundation
    IO: print() and input()
    Variables
    Objects and types
    Dynamic typing and None
### 2 - The string data type
    Literal string, f-string, format(), r-string
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
    Chained comparisons
    While loop
    For loop - the range() builtin function
    Jump in loop by break, continue, return
    Else in a loop statement

## Part 2 - Basic Data Structures

### 1 - List
    Mutable resizable sequence for the array ADT
    Literal definition and constructor
    Editing by methods and statement del
    Ordering by builtin sorted() and method sort()
    Unordering by random shuffle(), reversing by method reverse()
    List comprehension
    Shallow copy and deep copy
### 2 - Tuple
    Kind of an immutable list
    Literal definition
    Generator expression to emulate a tuple comprehension
### 3 - Dictionary
    Mutable collection of key-value pairs implementing the hashtable ADT
    Literal definition, constructor function, dictionary comprehension
    Accessing components by operator (not) in, [], method get()
    Editing components by assignment, setdefault(), pop(), ...
    Views by items(), keys(), values()
    Copies by copy(), dict(), deepcopy()
    Update by update() and merge by operator |
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
    Passing arguments by position and by keyword
    Parameter separators keyword-only and positional-only
    Default parameter value
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

## Part 4 - Persistence

### 1 - File
    The os module
    The shutil module
    open() / close(), with
    print(), write()
    read(), readlines(), readline(), for - in
    pathlib.Path
### 2 - Serialization
    CSV
    Reading from XLS and XLSX
    JSON
    XML
    struct
    pickle
    protobuf
### 3 - sqlite3
    Connection: connect(), cursor(), close()
    Cursor: execute(), close()
    Parametrized query as a way to defend against SQL injection attack
    Cursor (result): fetchone(), fetchmany(), fetchall(), rowcount, lastrowid
    Transaction (Connection): commit(), rollback()
### 4 - SQLAlchemy
    Engine: create_engine(), connect()
    Connection: execute(), text(), also for parameterized queries, close()
    CursorResult: fetchone(), fetchmany(), fetchall(), keys(), rowcount, lastrowid
    Transaction: Connection.begin(), commit(), rollback(), autocommit, Engine.begin()

## Part 5 - Deep Dive

### 1 - Numbers
    The Number hierarchy
    Built-in types: bool, int, float, complex
    Boolean: True/Truthy, False/Falsy; and, or, not, exor
    Integer: binary, octal, hexadecimal; underscore; division; module; power
    Float: literal definition; the constants epsilon, min, max, inf, nan
    Complex: real, imag, conjugate()
    Some useful built-in functions: abs(), divmod(), pow(), round()
### 2 - String
    Formatting in f-string
    Encode and decode
    Check: isalpha(), isdigit(), ...
    Search: find(), index(), ...
    Change: split(), join(), ...
### 3 - Function
    Packing and unpacking arguments
    Inner function and recursion
    Closure
    Decorator and class decorator
    Interaction with namespaces
    Some useful built-in functions: map(), filter(), reduce(), zip(), enumerate(), ...    
### 4 - Object Oriented Programming
    Class object and metaclass type
    Attributes and properties
    Private by naming convention and name mangling
    Methods: instance, class, static
    Special methods: __init__(), ...
    Multiple Inheritance: __bases__
    Method Resolution Order: mro() and __mro__
    Abstract Base Class (ABC) and @abstractmethod
### 5 - Iterators
    Iterables and iterators: __getitem__, __iter__, __next__
    Generator: yield, expression
    collections.abc: Iterable, Sized, Container, Reversible, Collection, Sequence
    Comprehension and generator for sequence definition
    Unpacking on iterables
### 6 - The collections module
    Counter
    defaultdict
    namedtuple
    deque

## Part 6 - Further Topics

### 1 - Code robustness: Exception, Log, and Test
    Exception: raise, try, except, else, finally
    Standard and custom exceptions
    Log: print() on stderr
    logging: getLogger(), debug(), ..., basicConfig()
    Unit Test
    unittest: assertions, discover tests
    VS Code and unittest
### 2 - Design Patterns
    Singleton
    Factory Method
### 3 - Concurrency
    Multithreading vs multiprocessing
    threading
    multiprocessing
    Asynchronous programming: async def, await,
    asyncio: run(), create_task(), gather()
### 4 - Web - REST API
    Flask - Web framework
    requests