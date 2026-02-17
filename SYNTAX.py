# i am good!!!
# day 10 ig of using git hub 
#the reason i am using it that i get a good looking dashboard and commmitments!!
print ("HEllo" == "Hello")
print ("HEllo" == "HEllo")
print(int(2.555))
#==================================
"""
Python Syntax Notes — concise reference

Keep this file as short, readable examples and reminders
covering common Python syntax and idioms.
"""

# -----------------------------
# Basics
# -----------------------------
# Comments: single-line uses #, multi-line docstrings use triple quotes.
# Indentation: use 4 spaces (significant; no braces).

# Variables and types (dynamic typing)
name = "Alice"      # str
age = 30             # int
pi = 3.1415          # float
enabled = True       # bool
nothing = None       # NoneType

# -----------------------------
# Strings
# -----------------------------
greeting = 'hello'
quote = "He said \"hi\""
multiline = '''line1
line2'''
fstring = f"{name} is {age} years old"
raw = r"C:\new\text"

# Common string methods: .upper(), .lower(), .strip(), .split(), .format(), f-strings

# -----------------------------
# Numbers & operators
# -----------------------------
sum_val = 1 + 2
prod = 2 * 3
exp = 2 ** 3        # power
floor_div = 7 // 2  # integer division
mod = 7 % 2

# Augmented assignment
count = 0
count += 1

# -----------------------------
# Collections
# -----------------------------
# List (mutable)
L = [1, 2, 3]
L.append(4)

# Tuple (immutable)
T = (1, 2, 3)

# Set (unique, unordered)
S = {1, 2, 3}

# Dict (mapping)
D = {"a": 1, "b": 2}
val = D.get("c", 0)

# Comprehensions
sq = [x*x for x in range(5)]
evens = {x for x in range(10) if x % 2 == 0}

# -----------------------------
# Control flow
# -----------------------------
if age >= 18:
    status = "adult"
elif age > 12:
    status = "teen"
else:
    status = "child"

for i in range(3):
    pass

while False:
    break

# for/else: else runs when loop didn't break
for x in [1, 2, 3]:
    if x == 0:
        break
else:
    did_break = False

# -----------------------------
# Functions
# -----------------------------
def add(a: int, b: int = 0) -> int:
    """Return sum of a and b."""
    return a + b

# Positional, *args, and **kwargs
def fn(*args, **kwargs):
    return args, kwargs

# Lambda (small anonymous functions)
mul = lambda x, y: x * y

# -----------------------------
# Modules & imports
# -----------------------------
import math
from collections import defaultdict as dd

if __name__ == "__main__":
    # run quick demo when executed directly
    print(fstring)

# -----------------------------
# Classes (basic)
# -----------------------------
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name}."

# Dataclasses (if available) provide boilerplate reduction
try:
    from dataclasses import dataclass

    @dataclass
    class Point:
        x: float
        y: float
except Exception:
    pass

# -----------------------------
# Exceptions
# -----------------------------
try:
    x = int("not an int")
except ValueError as e:
    # handle conversion error
    x = None
finally:
    # optional cleanup
    pass

# Raise errors
# raise ValueError("bad value")

# -----------------------------
# File I/O and context manager
# -----------------------------
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")

# -----------------------------
# Iterators & generators
# -----------------------------
def gen(n):
    for i in range(n):
        yield i

# Generator expression
gexpr = (x*x for x in range(5))

# -----------------------------
# Decorators (simple)
# -----------------------------
def decorate(fn):
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper

# -----------------------------
# Useful built-ins & idioms
# -----------------------------
# len(), range(), enumerate(), zip(), map(), filter(), sorted(), reversed()
# Unpacking: a, b = (1, 2); *rest = [1,2,3]
# Slicing: seq[start:stop:step]
# Ternary: x if cond else y
# Walrus operator (Python 3.8+): if (n := len(seq)) > 0:
# EAFP (easier to ask forgiveness than permission) is Pythonic

# -----------------------------
# Typing (optional hints)
# -----------------------------
from typing import List, Dict, Optional

# Example type hint: def make_list(n: int) -> List[int]:

# -----------------------------
# Style & tooling
# -----------------------------
# Follow PEP8: 4-space indentation, snake_case for functions/vars,
# CapWords for classes, limit lines to ~79-120 chars per project style.
# Use virtual environments: `python -m venv .venv` and `pip install -r requirements.txt`.

# End of concise syntax notes

#to repeat number of printed lines of same type and copies then
print("Hello, World!   \n"*5  )





