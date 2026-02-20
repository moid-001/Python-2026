"""
Python Fundamentals — concise notes and examples

Sections:
- Basics: interpreter, REPL, scripts
- Variables & Data Types
- Collections: list, tuple, set, dict
- Control Flow
- Functions
- Modules & Packages
- OOP basics
- Exceptions & File I/O
- Useful built-ins & stdlib notes

Read this file for quick reference and small examples.
"""

# --- Basics ---
# Run a script: `python fundamentals.py`
# Interactive REPL: run `python` or `python -i` for testing snippets.

# --- Variables & Data Types ---
# dynamic typing, assignment
name = "Alice"  # str
age = 30         # int
pi = 3.14159     # float
enabled = True   # bool

# Common type checks / conversions
is_str = isinstance(name, str)
age_str = str(age)
age_int = int(age)

# --- Collections ---
# List: ordered, mutable
fruits = ["apple", "banana", "cherry"]
fruits.append("date")

# Tuple: ordered, immutable
coords = (10, 20)

# Set: unordered, unique
letters = set(["a", "b", "a"])  # {'a','b'}

# Dict: key -> value mapping
user = {"id": 1, "name": "Alice"}
user["email"] = "alice@example.com"

# Comprehensions
squares = [x*x for x in range(6)]
even = {x for x in range(10) if x % 2 == 0}
mapping = {x: x*x for x in range(5)}

# --- Control Flow ---
if age >= 18:
    status = "adult"
elif age >= 13:
    status = "teen"
else:
    status = "child"

for i, f in enumerate(fruits, 1):
    pass  # iterate with index

while False:
    break

# --- Functions ---
def greet(name: str) -> str:
    """Return a greeting for `name`."""
    return f"Hello, {name}!"

def add(a: int, b: int = 0) -> int:
    return a + b

# Lambda (small anonymous function)
double = lambda x: x * 2

# --- Modules & Packages ---
# Import from stdlib or local modules
import os
from math import sqrt

# Create packages by adding an __init__.py file to a folder.

# --- OOP Basics ---
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name}."

# Inheritance
class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)
        self.student_id = student_id

# --- Exceptions & File I/O ---
try:
    with open("example.txt", "r", encoding="utf-8") as fh:
        data = fh.read()
except FileNotFoundError:
    data = ""
except Exception as e:
    raise

# Raising an exception
# raise ValueError("invalid value")

# --- Useful built-ins & stdlib notes ---
# built-ins: len(), range(), enumerate(), zip(), map(), filter(), sorted(), open()
# common stdlib: os, sys, pathlib, json, datetime, collections, itertools, functools

import json

# Example: json serialization
payload = {"user": "alice", "active": True}
json_str = json.dumps(payload)

# Virtual environments and package management
# - Create venv: `python -m venv .venv`
# - Activate (Windows PowerShell): `.\.venv\Scripts\Activate.ps1`
# - Install: `pip install <package>`

# --- Tips ---
# - Use type hints for clarity but they are optional at runtime.
# - Follow PEP 8 naming and formatting (use tools like `black`, `flake8`).
# - Write small functions, add docstrings, and keep modules focused.

# --- Quick reference examples ---
if __name__ == "__main__":
    print(greet("World"))
    print("Types:", type(name), type(age), type(fruits))
    print("Squares:", squares)

