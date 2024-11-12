### 1. Basics Syntax
# - Python is a widely used high-level programming language with a clean and readable syntax.
# - Comments start with `#` and are ignored by Python.
# - Indentation is used to define code blocks.
# - Python is case-sensitive, so `hello` and `Hello` are different variables.
# - Python is dynamically typed, which means you don't have to declare the data types of variables explicitly.
# - Print statements are used to display output in the console.

# This is a comment: Print 10
print(10)


### 2. Variables and Datatypes
# - Variables are created when you assign a value to them. You can change the value of a variable by assigning a new value to it.
# - Data Types are used to specify the type of values a variable can hold.
# - The Primary Data Types are:
#   - Numeric: int, float, complex
integer_dt: int = 10
float_dt: float = 10.5
complex_dt: complex = 10 + 5j
print(integer_dt, float_dt, complex_dt)

#   - String: str
string_dt: str = "Subrata Mondal"
print(string_dt)

#   - Sequence: list, tuple, range
list_dt: list = [1, 2, 3]
tuple_dt: tuple = (1, 2, 3)
range_dt: range = range(1, 10)
print(list_dt, tuple_dt, range_dt)

#   - Set: set, frozenset
set_dt: set = {1, 2, 3}
frozenset_dt: frozenset = frozenset({1, 2, 3})
print(set_dt, frozenset_dt)

#   - Mapping: dict
dict_dt: dict = {"a": 1, "b": 2, "c": 3}
print(dict_dt)

#   - Boolean: bool
bool_dt: bool = True
print(bool_dt)

#   - NoneType: None
none_dt: None = None
print(none_dt)

#   - Buffer: bytes, bytearray, memoryview
# bytes: a sequence of bytes is an immutable sequence of single bytes, often used to represent binary data.
bytes_dt: bytes = b"Hello, World!"

# Creating bytes
b1 = bytes([65, 66, 67])  # From a list of integers
b2 = b"ABC"  # From a string literal
b3 = bytes("ABC", "utf-8")  # From a string with encoding

print(b1)  # b'ABC'
print(b2)  # b'ABC'
print(b3)  # b'ABC'

# Accessing elements
print(b1[0])  # 65

# bytearray: a sequence of bytes is a mutable sequence of single bytes, often used to represent binary data.
bytearray_dt: bytearray = bytearray(b"Hello, World!")
# Creating bytearray
ba1 = bytearray([65, 66, 67])
ba2 = bytearray(b"ABC")

print(ba1)  # bytearray(b'ABC')

# Modifying bytearray
ba1[0] = 68
print(ba1)  # bytearray(b'DBC')

# Appending to bytearray
ba1.append(69)
print(ba1)  # bytearray(b'DBCE')

# memoryview: a sequence of bytes is a view of a memory region, often used to represent binary data.
memoryview_dt: memoryview = memoryview(b"Hello, World!")
print(bytes_dt, bytearray_dt, memoryview_dt)

# Creating memoryview
data = bytearray(b"Hello")
mv = memoryview(data)

# Accessing data
print(data)
print(mv[0])  # 72 (ASCII code for 'H')

# Modifying data through memoryview
mv[0] = 74  # ASCII code for 'J'
print(data)  # bytearray(b'Jello')

# Slicing memoryview
print(mv[1:3].tobytes())  # b'el'

# Creating a new bytearray from memoryview
new_data = bytearray(mv[1:4])
print(new_data)  # bytearray(b'ell')

# Converting memoryview to bytes
print(mv, mv.tobytes())

### 3. Conditional Statements
# - If-Else: used to define a condition and take an action if the condition is true, and another action if the condition is false.
if True:
    print("True")
else:
    print("False")

# - For Loop: used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.
for i in range(10):
    print(i)

# - While Loop: used to execute a block of code as long as a certain condition is true.
i = 0
while i < 10:
    print(i)
    i += 1

### 4. Type Casting
# - Type Casting is the process of converting a value from one data type to another data type.
# - Python provides the `int()`, `float()`, `complex()`, `str()`, `bool()`, `bytes()`, `bytearray()`, and `memoryview()` functions to perform type casting.

int_dt = 10
float_dt = float(int_dt)
complex_dt = complex(int_dt)
str_dt = str(int_dt)
bool_dt = bool(int_dt)
bytes_dt = bytes(int_dt)
bytearray_dt = bytearray(int_dt)
memoryview_dt = memoryview(bytearray_dt)

print(
    int_dt, float_dt, complex_dt, str_dt, bool_dt, bytes_dt, bytearray_dt, memoryview_dt
)

### 5. Exception Handling
# - Exception Handling is the process of handling errors or exceptions that may occur during the execution of a program.
# - Python provides the `try`, `except`, and `finally` keywords to handle exceptions.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Error: Division by zero")
    raise ZeroDivisionError("Na na na! Na na na!")
finally:
    print("Finally block executed no matter what")

### 6. Functions and built-in Functions
# - Functions: used to define a block of code that can be reused multiple times in a program.
# - Built-in Functions: are predefined functions that are part of the Python standard library and are available for use in any Python program.


def add(a, b):
    return a + b


print(add(2, 3))

# builtin functions
print(len("hello"))
print(max(1, 2, 3))
print(min(1, 2, 3))
print(sum([1, 2, 3]))
print(sorted([1, 2, 3]))
print(sorted([1, 2, 3], reverse=True))
print(sorted([1, 2, 3], key=lambda x: x * 2))
print(sorted([1, 2, 3], key=lambda x: x * 2, reverse=True))

# Sort a list of strings by length
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['date', 'apple', 'banana', 'cherry']

# Sort a list of tuples by the second element
pairs = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(4, 1), (3, 2), (1, 5), (2, 8)]

from operator import itemgetter

# Sort a list of dictionaries by a specific key
data = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
]
sorted_data = sorted(data, key=itemgetter("age"))
print(sorted_data)
# [{'name': 'Alice', 'age': 25}, {'name': 'John', 'age': 30}, {'name': 'Bob', 'age': 35}]

# Sort a list of dictionaries by a specific key in reverse order
data = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
]
sorted_data = sorted(data, key=itemgetter("age"), reverse=True)
print(sorted_data)
# [{'name': 'Bob', 'age': 35}, {'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]


### 7. Args and Kwargs
# - *args: used to pass a variable number of positional arguments to a function.
# - **kwargs: used to pass a variable number of keyword arguments to a function.


def greet(*names, greeting="Hello"):
    for name in names:
        print(f"{greeting}, {name}")


greet("Alice", "Bob", "Charlie")
greet("Alice", "Bob", "Charlie", greeting="Good Morning")


def greet_n(*names, greeting="Hello", **extrgreetings):
    for name in names:
        print(f"{greeting}, {name}")
    for key, value in extrgreetings.items():
        print(f"{key}: {value}")


greet_n("Alice", "Bob", "Charlie", greeting="Good Morning")
greet_n(
    "Alice",
    "Bob",
    "Charlie",
    greeting="Good Morning",
    Linda="Hola",
    Mike="Bonjour",
)

### 8. List, Tuples, Sets, Dictionaries
# - List: ordered, mutable, indexable and allows duplicate elements.
# - Tuple: ordered, immutable, indexable and allows duplicate elements.
# - Set: unordered, mutable, unindexable and doesn't allow duplicate elements.
# - Dictionary: unordered, mutable, indexable and allows duplicate keys.

# Creating a list
my_list = [1, 2, 3]
print(my_list)  # [1, 2, 3]

# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)  # (1, 2, 3)

# Creating a set
my_set = {1, 2, 3}
print(my_set)  # {1, 2, 3}

# Creating a dictionary
my_dict = {"name": "John", "age": 30}
print(my_dict)  # {'name': 'John', 'age': 30}

# Get all the keys of a dictionary
print(my_dict.keys())  # dict_keys(['name', 'age'])

# Get all the values of a dictionary
print(my_dict.values())  # dict_values(['John', 30])

# Get all the items (key-value pairs) of a dictionary
print(my_dict.items())  # dict_items([('name', 'John'), ('age', 30)])

# Pop an element from the dictionary
popped_element = my_dict.pop("name")
print(popped_element)  # John

### 9. List Comprehensions
# - List comprehensions are a way to create a new list by iterating over an existing list and applying a function to each element.
# - They are a concise and powerful way to create new lists in Python.
# - Syntax: [expression for item in iterable if condition]

# Creating a new list using list comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x * x for x in numbers if x * x > 5]
print(squared_numbers)  # [36, 49]

# Creating 2D list using list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [x for row in matrix for x in row]
print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create Matrix from the Flattened Matrix
matrix = [flattened_matrix[i : i + 3] for i in range(0, len(flattened_matrix), 3)]
print(matrix)

# Create a Matrix using list comprehensions
matrix = [[i + j for i in range(3)] for j in range(3)]
print(matrix)


### 10. Generators Expressions
# - Generator expressions are a way to create generators in Python.
# - They are a concise and powerful way to create generators in Python.
# - Syntax: (expression for item in iterable if condition)

# Creating a generator using generator expressions
squared_numbers = (x * x for x in range(10))
print(squared_numbers)
print(next(iter(squared_numbers)))


# Creating a generator using a function
def gen(n):
    for i in range(n):
        yield i


g = gen(10)
print(g)
print(next(g))

for i in g:
    print(i)

### 11. Lambda Functions
# Can have multiple arguments but only one expression
# - Lambda functions are a way to create small, anonymous functions in Python.
# - They are a concise and powerful way to create functions in Python.
# - Syntax: lambda arguments: expression

# Creating a lambda function
add = lambda x, y, z: x + y * z
print(add(2, 3, 4))


### 12. Decorators
# - Decorators modify functions using other functions.
# - Decorators are a way to add functionality to existing functions in Python.
# - They are a concise and powerful way to modify the behavior of functions in Python.
# - Syntax: @decorator


# Creating a decorator
def my_decorator(func):
    def wrapper(name):
        print("Wrapper: Before function call")
        func(name)
        print("Wrapper: After function call")

    return wrapper


def hello(name: str):
    print(f"Welcome: {name}")


use_decorator = my_decorator(hello)
use_decorator("Subrata Mondal")


@my_decorator
def hello(name: str):
    print(f"Welcome: {name}")


hello("Subrata Mondal")
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took {end_time - start_time} seconds to execute"
        )
        return result

    return wrapper


@timer
def my_function():
    time.sleep(2)


my_function()

### 13. Regex
# - Used for searching, matching and  manipulating strings.
# - Regular expressions (regex) are a way to match patterns in text.
# - They are a concise and powerful way to search and manipulate text in Python.
# - Syntax: re.match(pattern, string)
import re

matched = re.match(pattern=r"apple", string="I like apple")
print(matched)
# - Syntax: re.search(pattern, string)
searched = re.search(pattern=r"apple", string="I like apples")
print(searched)
# - Syntax: re.findall(pattern, string)
find = re.findall(
    pattern=r"apple", string="I like apples, red apples are the sweetest."
)
print(find)

find_int = re.findall(
    pattern=r"\d", string="I like 2 apples at rs 50, red apples are the sweetest."
)
print(find_int)


def has_uppercase(string):
    return bool(re.search(pattern=r"[A-Z]", string=string))


print(has_uppercase(string="Subrata"))

# - Syntax: re.sub(pattern, replacement, string)
subbed = re.sub(pattern=r"apple", repl="banana", string="I like apple")
print(subbed)
# - Syntax: re.split(pattern, string)
split = re.split(pattern=r"apple", string="I like apple")
print(split)
# - Syntax: re.compile(pattern)
compiled = re.compile(pattern=r"apple")
print(compiled)
# - Syntax: re.escape(string)
escaped = re.escape(pattern="I like apple")
print(escaped)
# - Syntax: re.IGNORECASE
ignore = re.IGNORECASE
print(ignore)


### 14. OOPs Concepts
# - Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to model real-world entities.
# - It provides a way to group related data and behavior into a single unit called a class.
# - It is a way to create reusable and maintainable code.
# - `self` is a reference to the current instance of a class.


class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def describe(self):
        return f"{self.name} is at level {self.level}"


# Creating an instance of the Hero class
hero = Hero(name="Subrata", level=10)
print(hero.name)
print(hero.level)
print(hero.describe())


# - Class Variables
class Hero:
    weight = 100

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def describe(self):
        return f"{self.name} is at level {self.level}"


hero1 = Hero(name="Subrata", level=10)
print(hero1.name)
print(hero1.level)
print(hero1.describe())
print("Hero.__dict__", Hero.__dict__)
print("hero1.__dict__", hero1.__dict__)

### 15. Inheritance
# - Inheritance is a way to create a new class based on an existing class.
# - It allows you to reuse the code and functionality of an existing class.
# - Syntax: class ChildClass(ParentClass):


class Archer(Hero):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.arrows = 10

    def describe(self):
        return super().describe() + " Archer with arrows: " + str(self.arrows)


archer = Archer(name="Robin", level=30)
print(archer.name)
print(archer.level)
print(archer.describe())


class Wizard(Hero):
    def describe(self):
        return super().describe() + " Wizard"


wizard = Wizard(name="Merlin", level=30)
print(wizard.name)
print(wizard.level)
print(wizard.describe())

### 16. Private Attributes, Getters and Setters
# - Private attributes are attributes that are not accessible outside of the class.
# - Getters and Setters are methods that are used to access and modify private attributes.
# - Syntax: _attribute


class Hero:
    def __init__(self, name, level):
        self._name = name
        self._level = level

    @property
    def level(self):
        print("Getter used")
        return self._level

    @level.setter
    def level(self, new_level):
        print("Setter used")
        if new_level > self._level:
            self._level = new_level
        else:
            print(f"Invalid level: {new_level} must be > {self._level}")

    def describe(self):
        return f"{self._name} is at level {self._level}"


hero = Hero(name="Subrata", level=10)
print(hero.level)
hero.level = 30
print(hero.level)
print(hero.describe())


### 17. Dunder Methods / Magic Methods
# - Dunder methods are methods that are called automatically by Python when an operation is performed on an object.
# - Syntax: __dunder_method__


# Example of Dunder Methods
class Vector:
    def __init__(self, x, y):
        """
        Initializes Vector with x and y coordinates.

        Parameters
        ----------
        x : int or float
            The x-coordinate of the vector.
        y : int or float
            The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v1 / 2)

### 18. Abstract Class and Methods
# - Abstract classes are classes that cannot be instantiated.
# - They are used to define a common interface for a set of related classes.
# - Abstract methods are methods that have no implementation in the abstract class.
# - They are used to enforce a common interface for a set of related classes.
# - Syntax: from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())


### 19. Type Hinting
# - Type hinting is a way to specify the type of a variable or function parameter.
# - It helps to catch errors and improve the readability of the code.
# - Syntax: variable_name: type

x: int = 5
y: str = "hello"


def greeting(name: str) -> None:
    print(f"Hello, {name}!")


greeting(name="John")


def add(a: int, b: int) -> int:
    return a + b


result: int = add(a=3, b=5)
print(result)

### 20. Custom Types with TypeVar
# - TypeVar is a generic type that can be used to create custom types.
# - It is used to define a type that can be used in multiple places in the code.
# - Syntax: from typing import TypeVar

from typing import TypeVar

T = TypeVar("T", bound="Animal")


class Animal:
    def sound(self) -> str:
        return ""


class Dog(Animal):
    def sound(self) -> str:
        return "Woof!"


def make_sound(animal: T) -> None:
    print(animal.sound())


make_sound(animal=Dog())


### 21. Modules and Packages
# - A module is a file containing Python code.
# - A package is a directory containing one or more modules.
# - Syntax: import module

### 22. Testing with Pytest
# - Pytest is a testing framework for Python.
# - It is used to write and run tests for Python code.
# - Syntax: pytest

import pytest


def add(a, b):
    """Add two numbers."""
    return a + b


class Calculator:
    """A simple calculator class."""

    def __init__(self):
        """Initialize the calculator."""
        self.result = 0

    def add(self, num):
        """Add a number to the result."""
        self.result += num

    def subtract(self, num):
        """Subtract a number from the result."""
        self.result -= num


@pytest.fixture
def calculator():
    """Return a new calculator instance."""
    return Calculator()


def test_add(calculator):
    """Test adding a number to the result."""
    calculator.add(5)
    assert calculator.result == 5


def test_subtract(calculator):
    """Test subtracting a number from the result."""
    calculator.subtract(2)
    assert calculator.result == -2


### 23. Tooling
# - Tooling is a set of tools that are used to help with the development of software.
# - It includes tools for testing, linting, formatting, and more.
# - Syntax: pip install tooling
