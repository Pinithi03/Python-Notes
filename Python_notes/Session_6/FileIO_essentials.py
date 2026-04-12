"""Opening and Closing Files Manually"""

# The basic way to work with files:
# Step 1: Open the file
from unicodedata import name


file = open("data.txt", "r")

# Step 2: Do something with the file
content = file.read()
print(content)

# Step 3: Close the file when done!
file.close()
#If you forget .close(): Problems with manual close:
# Easy to forget .close()
# If an error occurs before .close(), the file stays open
# Gets messy when working with multiple files

#When manual open/close can be useful:
#When you need a file open across different parts of your code
#When you want to understand what with does under the hood
#Quick interactive testing in the Python shell

#The with Statement (ALWAYS PREFER THIS!)
#Best practice: use with instead of manual open/close:
# BEST - File automatically closes
with open("data.txt", "r") as file:
    content = file.read()
# File is closed here automatically!

#File Modes
""" "r": Read. File must exist. Read-only.
- "w": Write. Creates new file. OVERWRITES existing!
- "a": Append. Creates if new. Adds to end.
- "r+": Read + Write. File must exist. Can read and write. """

"""Reading Files"""
#Method 1: read() - Entire File
# Reads entire file as one string
with open("data.txt", "r") as file:
    content = file.read()
print(content)

#Method 2: readlines() - List of Lines
# Reads all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()
print(lines)  # ["Line 1\\n", "Line 2\\n", "Line 3\\n"]
# Remove \\n with strip()
clean_lines = [line.strip() for line in lines]
print(clean_lines)  # ["Line 1", "Line 2", "Line 3"]

#Method 3: Iteration - Line by Line (BEST!)
# Most Pythonic and memory efficient
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
        
"""Writing Files"""
#Writing Text
# Write mode - creates / overwrites file
with open("output.txt", "w") as file:
    file.write("Hello, World!\\n")
    file.write("Second line\\n")


#Writing Multiple Lines
# Method 1: Write one by one
with open("output.txt", "w") as file:
    for item in ["Line 1", "Line 2", "Line 3"]:
        file.write(item + "\\n")

# Method 2: writelines() with \\n
lines = ["Line 1\\n", "Line 2\\n", "Line 3\\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)


#Appending to Files
# Append mode - adds to end without erasing
with open("log.txt", "a") as file:
    file.write("New entry\\n")
    
    
"""Working with Structured Data (CSV)"""
#CSV Format Basics
# CSV = Comma Separated Values
# Format:
# header1,header2,header3
# value1,value2,value3
# value4,value5,value6
# Example: students.csv
name,age,grade
Alice,20,85
Bob,21,92
Charlie,19,78


#Writing Dictionary to CSV
# Dictionary: {name: score}
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
}

# Save to CSV
with open("scores.csv", "w") as file:
    file.write("name,score\\n")
    for name, score in students.items():
        file.write(f"{name},{score}\\n")
# Result in file:
# name,score
# Alice,85
# Bob,92
# Charlie,78


#Reading CSV into Dictionary
# Load CSV into dictionary
students = {}
with open("scores.csv", "r") as file:
    lines = file.readlines()

# Skip header (first line)
for line in lines[1:]:
    name, score = line.strip().split(",")
    students[name] = int(score)

print(students)
# {"Alice": 85, "Bob": 92, "Charlie": 78}


#Writing List of Dictionaries
# List of dicts: [{"name": "Alice", "age": 20, "grade": 85}, ...]
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 21, "grade": 92},
]
# Save to CSV
with open("students.csv", "w") as file:
    file.write("name,age,grade\\n")
    for student in students:
        line = f"{student['name']},{student['age']},{student['grade']}\\n"
        file.write(line)
        
#Reading CSV into List of Dictionaries
# Load into list of dicts
students = []
with open("students.csv", "r") as file:
    lines = file.readlines()

# Skip header
for line in lines[1:]:
    name, age, grade = line.strip().split(",")
    student = {
        "name": name,
        "age": int(age),
        "grade": int(grade),
    }
    students.append(student)
print(students)
# [{"name": "Alice", "age": 20, "grade": 85}, ...]


#Essential String Methods for File I/O
#strip() - Remove Whitespace
# Removes spaces, \\n, \\t from both ends
text = " Hello World! \\n "
clean = text.strip()
print(clean)  # "Hello World!"

# ALWAYS use strip() when reading lines!
with open("data.txt", "r") as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)
        
#split() - Parse CSV
# Split string by delimiter
line = "Alice,85,20"
parts = line.split(",")
print(parts)  # ["Alice", "85", "20"]

# Unpack values
name, score, age = line.split(",")
print(name)   # "Alice"
print(score)  # "85" (string!)

# Convert types
score = int(score)


#join() - Create CSV
# Combine list into string
scores = [85, 92, 78, 88]
scores_str = ",".join(map(str, scores))
print(scores_str)  # "85,92,78,88"

# Use in file writing
with open("scores.txt", "w") as file:
    file.write(scores_str + "\\n")
    
"""Error Handling"""
#FileNotFoundError
# Handle missing files gracefully
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Creating new file...")
    with open("data.txt", "w") as file:
        file.write("Default content\\n")


#Check if File Exists
import os
# Check before opening
if os.path.exists("data.txt"):
    print("File exists!")
    with open("data.txt", "r") as file:
        content = file.read()
else:
    print("File doesn't exist. Creating...")
    with open("data.txt", "w") as file:
        file.write("New file\\n")


#Robust File Loading Pattern
def load_data(filename):
    """Load data from file, return empty dict if file missing."""
    try:
        with open(filename, "r") as file:
            data = {}
            return data
    except FileNotFoundError:
        return {}


# Use it
data = load_data("data.csv")
# Will never crash! Returns {} if file missing


"""Common Patterns"""
#Pattern 1: Save and Load Dictionary
# Save
def save_dict(data, filename):
    with open(filename, "w") as file:
        file.write("key,value\\n")
        for key, value in data.items():
            file.write(f"{key},{value}\\n")


# Load
def load_dict(filename):
    try:
        data = {}
        with open(filename, "r") as file:
            lines = file.readlines()[1:]  # Skip header
            for line in lines:
                key, value = line.strip().split(",")
                data[key] = value
        return data
    except FileNotFoundError:
        return {}

#Pattern 2: Save List as CSV
# Save list of numbers
def save_list(data, filename):
    with open(filename, "w") as file:
        line = ",".join(map(str, data))
        file.write(line + "\\n")


# Load list
def load_list(filename):
    try:
        with open(filename, "r") as file:
            line = file.read().strip()
        data = list(map(int, line.split(",")))
        return data
    except FileNotFoundError:
        return []
    
#Pattern 3: Append Log Entry
from datetime import datetime

def log(message, filename="log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {message}\\n")


# Usage
log("Application started")
log("User logged in")
log("File uploaded")

