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