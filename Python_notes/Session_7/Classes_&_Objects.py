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