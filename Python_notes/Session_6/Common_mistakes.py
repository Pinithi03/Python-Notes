"""Common Mistakes & Solutions"""
#1. Forgetting to add \\n
# WRONG - Everything on one line
file.write("Line 1")
file.write("Line 2")

# CORRECT - Add \n
file.write("Line 1\n")
file.write("Line 2\n")

#2. Not using strip() before split()
# WRONG - \\n causes issues
line = "Alice,85\\n"
name, score = line.split(",")
score = int(score)  # This works here, but strip() is still better practice

# CORRECT - Strip first
line = line.strip()
name, score = line.split(",")
score = int(score)

#3. Forgetting type conversion
# WRONG - Everything from file is string!
line = "85"
# total = line + 10  # Error! Can't add string + int

# CORRECT - Convert first
score = int(line)
total = score + 10

#4. Using "w" when you meant "a"
# WRONG - Erases file every time!
with open("log.txt", "w") as file:
    file.write("New entry\\n")

# CORRECT - Append to keep existing
with open("log.txt", "a") as file:
    file.write("New entry\\n")