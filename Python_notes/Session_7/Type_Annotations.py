"""What Are Type Annotations?
Type annotations tell Python (and other developers) what types your variables, parameters, and
return values should be. They are hints — Python does not enforce them at runtime. They
improve readability, documentation, and IDE support."""

# Basic Syntax
# Variable annotations
name: str = "Alice"
age: int = 20
gpa: float = 3.85
is_active: bool = True

# Function annotations (parameters + return type)
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_passing(score: float) -> bool:
    return score >= 60.0

# None return type (function doesn't return anything useful)
def display(message: str) -> None:
    print(message)


# Usage
print(greet("Alice"))
print(add(5, 3))
print(is_passing(75.5))
display("Welcome!")

"""Collections and Optional"""
from typing import Optional

# Lists - specify what’s inside the list
scores: list[int] = [85, 92, 78]
names: list[str] = ["Alice", "Bob"]

# Dictionaries - key and value types
student_scores: dict[str, int] = {"Alice": 85, "Bob": 92}

# Optional - value can be type OR None
def safe_divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

# Default parameters with annotations
def get_greeting(name: str, excited: bool = False) -> str:
    if excited:
        return f"Hello, {name}!!!"
    return f"Hello, {name}."

#Type Annotations in Classes
class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.grades: list[float] = []

    def add_grade(self, grade: float) -> None:
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be 0-100!")
        self.grades.append(grade)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    @property
    def letter_grade(self) -> str:
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self) -> str:
        return f"Student ({self.name}, Age {self.age})"
    
"""1. Typed constructor
def __init__(self, name: str, age: int) -> None:
Means:
name must be string
age must be int
returns nothing (None)"""

"""2. Typed attributes
self.grades: list[float] = []
Means:
this list only stores floats"""

"""3. Method return types
def get_average(self) -> float:
Means:
returns a float number"""

"""4. Property typing
def letter_grade(self) -> str:
Clean + readable API"""

"""Remember
• : type after parameters — def greet(name: str)
• -> type for return values — def greet(name: str) -> str:
• -> None for functions that don’t return anything
• Annotations are hints — Python won’t crash if you pass the wrong type
• Use Optional[type] when a value could be None"""

"""Combining Error Handling with Classes"""
class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self._balance = balance
        self._transactions = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self._balance += amount
        self._transactions.append(f"+${amount:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive!")
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount
        self._transactions.append(f"-${amount:.2f}")

    def __str__(self) -> str:
        return f"Account({self.owner}, Balance: ${self._balance:.2f})"
    
    """Common mistakes and Solutions"""
#1. Catching too broadly
#BAD:
try:
    complex_code()
except:
    pass   # Silent failure (dangerous)

#GOOD:
try:
    complex_code()
except ValueError:
    print("Invalid value!")
except FileNotFoundError:
    print("File not found!")
    
#2. Forgetting Self
#Bad
class Dog:
    def bark():
        print("Woof")
        
#Good
class Dog:
    def bark(self):
        print("Woof")
        
#3.Forgetting self. for attributes
#Bad
class Student:
    def __init__(self, name):
        name = name   # ❌ only local variable
        
#Good
class Student:
    def __init__(self, name):
        self.name = name   # stored in object

#4. Confusing Class vs Instance
class Car:
    def __init__(self, brand):
        self.brand = brand
my_car = Car("Toyota")
your_car = Car("Honda")
# Car is the class
# my_car is an instance ( object )