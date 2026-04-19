"""Class = Blueprint (template for creating objects)
Object = Instance (actual thing created from the blueprint)
Example:
• Class Car = the design/blueprint
• Object my car = Car("Toyota") = an actual car
• One class can create MANY objects!"""

# Creating a simple class
import __main__


class Student:
    def __init__(self, name, age):
        # Constructor runs when object is created
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
        self.grades = []      # Default attribute (empty list)

# Creating objects (instances)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

# Each object has its OWN attributes
print(alice.name)    # Alice
print(bob.name)      # Bob
print(alice.grades)  # []

#Adding methods
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        """Add a grade (method = function in a class)"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be 0-100!")

    def get_average(self):
        """Calculate average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Convert average to letter grade"""
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


# Using the class
student1 = Student("Alice", 20)

student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

print("Name:", student1.name)
print("Average:", student1.get_average())
print("Grade:", student1.get_letter_grade())

#__str__method 
"""__str__ is a special method (dunder method) in Python

It controls what happens when you do:
print(object)"""

#Without __str__
#__main__.Student object at 0x123456

#With __str__
#Student (Alice, Age 20, Avg: 85.0)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """Controls what print(object) shows"""
        avg = self.get_average()
        return f"Student ({self.name}, Age {self.age}, Avg: {avg:.1f})"


# Create object
alice = Student("Alice", 20)
alice.grades = [85, 92, 78]

# Print object
print(alice)

"""Decorators"""
#@property — Calculated Attributes
#It lets you use a method like an attribute

#Without @property
#alice.get_average()

#With @property
#alice.average   # cleaner 

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    @property
    def average(self):
        """Access like an attribute (no parentheses!)"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    @property
    def letter_grade(self):
        avg = self.average  # using another property
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


# Usage
alice = Student("Alice")
alice.grades = [85, 92, 78]

# Use WITHOUT parentheses
print(alice.average)       # 85.0
print(alice.letter_grade)  # B

"""@property makes methods look like attributes!
Without: alice.get average() — looks like a function call
With: alice.average — looks like accessing data (cleaner!)"""

"""When to Use @property
1. Data Validation: Ensure assigned values meet conditions (e.g., score must be 0–100)
2. Computed Attributes: Value calculated dynamically from other attributes (e.g., diam-
eter from radius)
3. Read-Only Properties: Attributes that can be accessed but not modified
4. Backward Compatibility: Convert a simple attribute to a property with logic — users
keep using the same object.attribute syntax"""


"""@property with Getter, Setter, and Deleter"""
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # "private" internal attribute

    @property
    def celsius(self):
        """Getter: called when you access t.celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter: called when you assign t.celsius = value"""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        """Deleter: called when you use del t.celsius"""
        print("Deleting value...")
        del self._celsius


# Usage
t = Temperature(25)

print(t.celsius)   # Getter -> 25

t.celsius = 30     # Setter -> valid
print(t.celsius)   # 30

# t.celsius = -300  # raises ValueError

del t.celsius      # Deleter

"""• @property — defines the getter (called on read: t.celsius)
• @name.setter — defines the setter (called on assignment: t.celsius = 30)
• @name.deleter — defines the deleter (called on delete: del t.celsius)
The property decorator works with “private” internal attributes named with a leading underscore
(e.g., celsius)."""

"""@staticmethod — Utility Functions"""
class MathHelper:

    @staticmethod
    def is_even(number):
        """Doesn’t need self - utility function"""
        return number % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Call WITHOUT creating an instance
print(MathHelper.is_even(4))   # True
print(MathHelper.factorial(5)) # 120


"""Complete Example: BankAccount"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance          # "private" convention
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @property
    def status(self):
        if self._balance < 0:
            return "Overdrawn"
        elif self._balance < 100:
            return "Low"
        else:
            return "Good"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self._balance += amount
        self._transactions.append(f"+ ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive!")
        if amount > self._balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount
        self._transactions.append(f"- ${amount:.2f}")

    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    def __str__(self):
        return f"Account ({self.owner}, ${self.balance:.2f}, {self.status})"


# Usage
acc = BankAccount("Alice", 500)

acc.deposit(100)

print(acc)            # Account (Alice, $600.00, Good)
print(acc.balance)    # 600
print(acc.status)     # Good