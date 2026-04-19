"""Class = Blueprint (template for creating objects)
Object = Instance (actual thing created from the blueprint)
Example:
• Class Car = the design/blueprint
• Object my car = Car("Toyota") = an actual car
• One class can create MANY objects!"""

# Creating a simple class
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